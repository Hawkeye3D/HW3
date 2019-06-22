import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
import calendar
def dfviewer(Df):
    print("Df.values: Return a Numpy representation of the DataFrame.")
    print(df.head(5))
    print('_______________')
    print("DF.index: The index (row labels) of the DataFrame.")
    print( (df.axes.index) )
    print('_______________')
    print("DF.axes: 	Return a list representing the axes of the DataFrame.")
    print( df.axes)
    print('_______________')
    print("DF.Ftypes: Return the ftypes (indication of sparse/dense and dtype) in DataFrame")
    print('Ftypes: '+ df.ftypes)
    print('_______________')
    print("Ftypes Count: Return counts of unique dtypes in this object.")
    print(df.get_dtype_counts())
    print('_______________')
    print("Df.ndim:  Return an int representing the number of axes / array dimensions.")
    print(df.ndim)
    print('_______________')
    print("Df.size:  Return an int representing the number of elements in this object.")
    print(df.size)
    print('_______________')
    print("Df.Shape:  Return a tuple representing the dimensionality of the DataFrame.")
    print(df.shape)
    print(df.shape.count)
    print(df.shape.index)
    print ('This is a tuple {0}'.format(df.shape))
    print('_______________')
    print("Df.empty:  Return an int representing the number of elements in this object.")
    print(df.empty)
    print('_______________')
    print("Df.memory_usage:  Return the memory usage of each column in bytes.")
    print(df.memory_usage)
    print('_______________')
    return;