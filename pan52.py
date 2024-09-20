"""20. Write a Pandas program 
to find average consumption of wine per person greater
 than 2 in world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[((a["Beverage Types"]=="Wine")&(a["Display Value"]>2))])