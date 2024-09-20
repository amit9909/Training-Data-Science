"""19. Write a Pandas program to filter all records where the 
average consumption of beverages per person from .5 to 2.50 in
 world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["Display Value"]>=0.5)&(a["Display Value"]<=2.50)])