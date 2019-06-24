#%%
import pandas as pd
from pandas import pivot_table, DataFrame, crosstab
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
import calendar
import sys
import collections
import generalfunctions #FINALLY works-barbaric case sensitivity!

def MyMax(val, comp):
    if val >= comp:
        return val
    elif val < comp:
        return comp


def MyMin(val, comp):
    if val <= comp:
        return val
    elif val > comp:
        return comp


def SortCsvFile(inputname, sortcolumn, outputfilename):
    with open(inputname, 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        data = sorted(csv_input, key=lambda row: (row[sortcolumn], row['X']))

    with open(outputfilename, 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)
# this routine expects to have
def writedicttofile(outputfilename,inputname):
       with open(inputname, 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        with open(outputfilename, 'w', newline='') as f_output:
            csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
            csv_output.writeheader()
            csv_output.writerows()
# zeros out copy of the Canidates List
def initCandiatesforCount(Canidates):
    ret = Canidates.copy
    ret = {x: 0 for x in Canidates}
    return ret

 
# File moved to local directory instead of using os.path.join(...),which is problematic
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
print
print

# This is a good way of transposing the output of the Dictionary into a
# more readable format. Fiddling around with the format strings would
# create a better looking table-like format, if desired.  I didn't desire it.

for key, value in Canidatecount.items():
    print(key + ": {:13d}".format(value) +
          " -->>> Percentage of vote: {:.2f}".format(value/cnt*100) + "%")
#
#
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
cnt -= 1  # over counted by 1, so backup
print("County breakdown")
print
# !!!!!The output is not pretty but is squares with the previous summary, 
# so now we know how many people voted for each canidate in each county!!
# AND THE RUSSIANS WERE NOT INVOLVED
print(Countycount)
for key, value in Countycount.items():
    print(key + " County---------------------------")
    for key2, value2 in value.items():
        print(key2 + ": {:13d}".format(value2))
    #end for    
#end for

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