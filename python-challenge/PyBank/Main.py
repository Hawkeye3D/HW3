import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
df['change'] = df['Profit/Losses']

mvalue = fd['Profit/Losses'].max()
minvalue = fd['Profit/Losses'].min()
sumvalue = fd.sum(axis=1,skipna = True)
index = ['Profit/Losses']
#avgvalue = fd['Profit/Losses'].avg()
#stdvalue = fd['Profit/Losses'].stdev()

print(mvalue,minvalue,Total,index) #,avgvalue,stdvalue)
 