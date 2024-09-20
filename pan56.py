"""24. Write a Pandas program to find which years have all non-zero values
 and which years have any non-zero values from world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["Display Value"]==0,["Year"])])
print(a.loc[(a["Display Value"]!=0,["Year"])])
