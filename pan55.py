"""23. Write a Pandas program to rename all and only some of the
 column names from world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
a=a.rename(columns = {"WHO region":"WHO_region","Display Value":"Display_Value"})
print(a)