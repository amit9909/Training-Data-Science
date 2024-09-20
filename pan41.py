"""write a pandas program to find out the alcohol consumption details in the year '1986'
 where who region is 'western pacific' 
   and country is 'vietNam' from the world alcohol consumptionn dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["WHO region"]=="Western Pacific") & (a["Country"]=="Viet Nam")& (a["Year"]==1986)])
