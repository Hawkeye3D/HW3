# %%
import pandas as pd
from pandas import pivot_table, DataFrame, crosstab
import numpy as np
import os
import csv
import string

# import us_state_abbrev

# would not import using import
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
AL = {"Emp ID": "Emp ID",
    "First Name": "FN",
    "Last Name": "Name",
    "DOB": "DOB",
    "SSN": "SSN",
    "State": "State"}
OR = ["Emp ID",
    "First Name",
    "Last Name",
    "DOB",
    "SSN",
    "State"]

def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]


# File moved to local directory instead of using os.path.join(...),which is problematic
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