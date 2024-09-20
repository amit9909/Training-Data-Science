"""18. Write a Pandas program to filter those records which not
 appears in a given list from world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["Display Value"]==0)])