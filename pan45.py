"""13. Write a Pandas program to find out the records where consumption
 of beverages per person average >=5 and Beverage Types
   is Beer from world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["Display Value"]>=5)&(a["Beverage Types"]=="Beer")])