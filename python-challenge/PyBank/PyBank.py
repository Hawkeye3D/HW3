import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
import calendar
import sys
 

 


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
  
