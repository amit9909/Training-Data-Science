"""22. Write a Pandas program to select consecutive columns and also
 select rows with Index label 0 to 9 with some columns 
 from world alcohol consumption dataset."""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.head())
print(a.loc[:,"Country":"Display Value"])
print(a.iloc[:,2:5].head())
print(a.loc[0:9,["Year","Country","Display Value"]])