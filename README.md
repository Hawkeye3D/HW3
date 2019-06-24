# HW3
[PyBank Code](pybank-code)
## Homework for Week3 - Rice Data Analytics
### PyBank Code
The main thing I did here was create a couple of helper definitions for Min and Max.  I generally find that easier than looking for the optimum way of doing it with native functions, unless speed is the issue.
The code is as code is as follows:


```python
def MyMax(val,comp):
    if val >= comp:
       return val
    elif val<comp:
        return comp
def MyMin(val,comp):
    if val <= comp:
       return val
    elif val>comp:
        return comp    
 
flocation = 'budget_data.csv' #File moved to local directory instead of using os.path.join(...),which is problematic
df = pd.read_csv(flocation)  
# #df.columns = ["Date","Profit/Losses"]#,"change"]bash
# dfviewer(df)

# df['Date']=pd.to_datetime(df['Date'])
Total = df['Profit/Losses'].sum()
 #lastrevenue = df['Profit/Losses']
mvalue = df['Profit/Losses'].max()
minvalue = df['Profit/Losses'].min()  
 
print(mvalue,minvalue, Total)  # ,avgvalue,stdvalue)

#use a dictionary to carry the values for the output
OutDict ={"Total_Months":-1,"Tot_Profit_Loss":0,"Average_Change":0,"GreatestInc":0,"GreatestDec":0}
#Opens file for 'r'eading - safest technique for open and closing files as will always close even if there is an exception
#thereby not hanging the os and losing the file
with open(flocation,'r') as infile:
  csvrows = csv.reader(infile, delimiter=',')  
  total=0
  cnt=0
  lastprofit=0
  maxprofit =-99999999999
  minprofit =9999999999
  sumdiff=0
  firstprofit=0
  for row in csvrows:
    OutDict["Total_Months"]+=1 #method 1 of summarizing count
    if cnt>0:  
        if cnt==1:
            firstprofit = float(row[1])   #subtract this value from the average difference numerator 
        #end if
        diff=(float(row[1])-lastprofit)
        maxprofit= MyMax(diff,maxprofit)
        minprofit= MyMin(diff,minprofit)
        sumdiff +=diff
        lastprofit=float(row[1])
        total += lastprofit         
    elif cnt==0:#skips header
        total=0
    #end if
    cnt+=1 #method 2 of summarizing count
  #end of for loop 
#End With
cnt-=1 #over counted by 1, so backup
 
OutDict["Tot_Profit_Loss"]=total
#defend against dividing by zero
if cnt>0:
  OutDict["Average_Change"]=(sumdiff-firstprofit)/cnt
elif cnt==0:
  OutDict["Average_Change"]=0
#end if
#   
OutDict["GreatestInc"]=maxprofit
OutDict["GreatestDec"]=minprofit   
print(OutDict)
print()
```
## PyPoll Code

This was the most fun to work on, simply because it is a very long set of records and I thought it was going to be really slow with Python code, but it really wasn't, so that was a nice surprise.  Still slow, but not painfully.  Anyway, the base problem was to count the number of counts for each candidate.  I did it with the following code:
```python
flocation = 'employee_data.csv'
# Using Panda
# df = pd.read_csv(flocation)
# dfviewer(df)
# SortCsvFile(flocation,'County','sortedbycount.csv')

Canidatecount = {}  # Dictionary of Individual
# Opens file for 'r'eading - safest technique for open and closing files as will always close even if there is an exception
# thereby not hanging the os and losing the file
with open(flocation, 'r') as infile:
    csvrows = csv.reader(infile, delimiter=',')

    cnt = 0

    for row in csvrows:
        if cnt > 0:
            if row[2] in Canidatecount:  # syntax to see if the item is in the dictionary
                Canidatecount[row[2]] += 1
            else:
                Canidatecount[row[2]] = 1
            # end IF
        # end if
        cnt += 1  # method 2 of summarizing count
    # end of for loop
# End With
cnt -= 1  # over counted by 1, so backup
print("Election count:" + str(cnt))
```
The code works by establishing a dictionary of {Canditatename:count}
Looping, the code first looks to see if the dictionary item exists or not
If so, then the count is incremented for that canditate.  If not, a new
entry to the dictionary is entered with a count of 1. And the loop goes
and goes.  I feel more comfortable using a loop counter to deal with 
the header issue, at least for now.

I did a couple of other things on this code, the question I had was how many votes did each candidate get in each county?
This required a dictionary in a dictionary approach which can be seen in the following code:
```python
# OK, now By County,Canidate Since we already have all of the
# canidates who have received votes in the state we will assign that empty list to
# each county as they are identified.  So the dictionary for the county is {Countyname,{Canidate Dictionary}}
cnt = 0
Countycount = {}  # initialize the county dictionary
with open(flocation, 'r') as infile:
    csvrows = csv.reader(infile, delimiter=',')

    cnt = 0 

    for row in csvrows:
        if cnt > 0:
            if row[1] in Countycount:  # syntax to see if the item is in the dictionary
               # temp={}
                temp = Countycount[row[1]]
                temp[row[2]] += 1
                Countycount[row[1]] = temp  # this should increment the proper
            else:  # new county, not in list needs to be added with a zeroed out Canidate list
                virgincanidatelist = initCandiatesforCount(
                    Canidatecount)  # setup clean slate                
                # init first count for whoever is the first candiate on the first county
                virgincanidatelist[row[2]]+=1
                Countycount[row[1]] = virgincanidatelist 
            # end IF
        # end if
        cnt += 1  # method 2 of summarizing count
    # end of for loop
# End With

```
It seems a bit clumsy to me, but it works just fine
And last but not least, PANDAMONIUM!
In Excel this problem would be handled (if it could manage the file size)
with pivottables, so I thought I should give it a google or two with Pandas.
Once I got the imports down, there were essentially *TWO* lines of code that created
a comprehensive, sub totaled, grand totaled grid, lickity-split!
The code:
```python
#
#  NOW, fun with Pandas and Pivot Tables!
#
#First, get a dataframe from the CSV File
#Note: The following was enabled by the following imports
# import pandas as pd
# from pandas import pivot_table, DataFrame, crosstab
# import numpy as np
df=pd.read_csv(flocation,delimiter=",") # where pd is the assigned name for my Pandas object
Df_pv = (pivot_table(df,index=['Candidate'], columns=['County'], aggfunc=np.count_nonzero,margins=True,margins_name='Totals'))
print(Df_pv)
#sans margin
Df_pv2 = (pivot_table(df,index=['Candidate'], columns=['County'], aggfunc=np.count_nonzero))#,margins=True,margins_name='Totals'))
Df_pv2.plot(kind='bar', stacked=True)
Df_pv2.plot.show()
 #print(df.head(5)) #take a look at the heading
print
print(" --- PANDAMONIUM! --- Over 100 lines of looping code replaced by 5 lines of code(including the imports!) ")
```

## PyBoss Code
```python
flocation = 'employee_data.csv'


EmployeeList = []  # Dictionary of Individual
NewEmployeeList = []
# Opens file for 'r'eading - safest technique for open and closing files as will always close even if there is an exception
# thereby not hanging the os and losing the file
with open(flocation, 'r') as infile:
    csv_input = csv.reader(infile, delimiter=',')
    EmployeeList = list(csv_input)
    #NewEmployeelist = EmployeeList[:]  # creates a duplicate of Employeelist   not used in this case since I need to insert a column
    #and there does not seem to be an elegant way of doing it - tried comprehension but it kept crashing.
    rowcnt = 0
    for i in EmployeeList:        
        #Append will append a single item to the list, in this case I am
        #appending a modified row list as indicated by the brackets.
        #if I used parenthesis I would be creating a tuple, except in that
        #case I can't modify any of the elements, which is a problem in this case
        NewEmployeeList.append([i[0],'First Name', i[1], i[2], i[3],i[4]])
    for row in NewEmployeeList:
        if rowcnt==0:
            row[2]="Last Name"
            print(row)
            rowcnt+=1
            continue #continue on with the loop
        words = row[2].split(  )  #make a list of the whitespace separated items
        if len(words) > 1: # I did't complete for the idea that a name would have less than two names
            row[1] = words[1] #first name
            row[2] = words[0] #redefine the name, renamed to Last name, that the parsed last name
            ds=row[3].split("-")#split on the hyphen
            row[3]=ds[1]+"/"+ds[2]+"/"+ds[0] # glue the split back in a different order
            row[4] = "***-**-" + right(row[4],4) # used a def for slice the right 4 characters
            #I tried doing all of this strState in one line by Python kept barfing on me, so I 
            #broke it up into more manageable pieces
            strState=row[5]
            strState=strState.lower()
            strState=strState.title()            
            strState=us_state_abbrev[strState]
            row[5] = strState
            print(row)
            rowcnt+=1
print('-')
print('-')
print("There are " + str(rowcnt-1) + " employees registered in this file at the moment")
```
The comments in the code explain this one. I tried a couple of approaches on this before I settled on this solution.  I also made the problem a bit more complex than it needed to be my thinking that dates should be treated as date-types and that obfuscated passwords and social security numbers should have some type of cryptography, but I didn't go too far down those rabbit holes.  The most interest code here is the .APPEND in line 199.  Append can append one object, be it a string, a number or a list. If you want to edit the items in the list,then make sure it is not a tuple.  I fiddled with that problem for a bit.
