#how to count the frequency of unique values in numpy array
import numpy as n
x=n.array([12,12,4,6,5,87,2,8,2,3,4,54,2,3,4,52,8,5,2,3,4,8,7,5])
y=n.unique(x,return_counts=True)
