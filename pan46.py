"""14. Write a Pandas program to find out the records where consumption of
 beverages per person average >=4 and Beverage Types is Beer, Wine, Spirits
from world alcohol consumption dataset.
Test Data:"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["Display Value"]>=4)&((a["Beverage Types"]=="Beer")
            |(a["Beverage Types"]=="Wine")|(a["Beverage Types"]=="Spirits"))])