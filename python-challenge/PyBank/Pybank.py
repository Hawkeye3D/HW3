import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
import calendar
import sys
 

 
<<<<<<< HEAD:python-challenge/PyBank/Pybank.py
# def dfviewer(df):
#     print("Df.values: Return a Numpy representation of the DataFrame.")
#     print(df.head(5))
#     print('_______________')
#     print("DF.index: The index (row labels) of the DataFrame.")
#     print( (df.axes.index) )
#     print('_______________')
#     print("DF.axes: 	Return a list representing the axes of the DataFrame.")
#     print( df.axes)
#     print('_______________')
#     print("DF.Ftypes: Return the ftypes (indication of sparse/dense and dtype) in DataFrame")
#     print('Ftypes: '+ df.ftypes)
#     print('_______________')
#     print("Ftypes Count: Return counts of unique dtypes in this object.")
#     print(df.get_dtype_counts())
#     print('_______________')
#     print("Df.ndim:  Return an int representing the number of axes / array dimensions.")
#     print(df.ndim)
#     print('_______________')
#     print("Df.size:  Return an int representing the number of elements in this object.")
#     print(df.size)
#     print('_______________')
#     print("Df.Shape:  Return a tuple representing the dimensionality of the DataFrame.")
#     print(df.shape)
#     print(df.shape.count)
#     print(df.shape.index)
#     print ('This is a tuple {0}'.format(df.shape))
#     print('_______________')
#     print("Df.empty:  Return an int representing the number of elements in this object.")
#     print(df.empty)
#     print('_______________')
#     print("Df.memory_usage:  Return the memory usage of each column in bytes.")
#     print(df.memory_usage)
#     print('_______________')
#     return
=======

>>>>>>> 69fd004f47d65afa9bb87107a16310b3ace717c5:python-challenge/PyBank/PyBank.py

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
  
