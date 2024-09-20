"""15. Write a Pandas program to filter
 the specified columns and records by range from
   world alcohol consumption dataset."""

import pandas as pd
a=pd.read_csv("kumar.csv")
num=input("enter your specified column :")
print(a.head())
print(a.loc[0:4, ["WHO region", "Beverage Types"]])
