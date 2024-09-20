"""25. Write a Pandas program to filter all columns where all entries present,
 check which rows and columns has a NaN and finally drop rows with any NaNs
   from world alcohol consumption dataset."""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[a["Year"].isna()])
print(a.loc[a["WHO region"].isna()])
print(a.loc[a["Country"].isna()])
print(a.loc[a["Beverage Types"].isna()])
print(a.loc[a["Display Value"].isna()])
a=a.dropna()
print(a)