import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
import calendar
import sys
   

 
# def dfviewer(Df):
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
def SortCsvFile(inputname,sortcolumn,outputfilename):  
    with open(inputname, 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        data = sorted(csv_input, key=lambda row: (row[sortcolumn], row['X']))

    with open(outputfilename, 'w', newline='') as f_output:    
        csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)        
 
flocation = 'election_data.csv' #File moved to local directory instead of using os.path.join(...),which is problematic
#Using Panda
#df = pd.read_csv(flocation)   
#dfviewer(df)

#SortCsvFile(flocation,'County','sortedbycount.csv')
ElectionCount={} #Dictionary of Individual 
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
      if cnt>0:
        if row[2] in ElectionCount:
            ElectionCount[row[2]]+=1
        else:
            ElectionCount[row[2]]=1
        #end IF 
      #end if    
      cnt+=1 #method 2 of summarizing count
  #end of for loop 
#End With
cnt-=1 #over counted by 1, so backup
print("Election count:" + str(cnt) )
print(ElectionCount)
