"""12. Write a Pandas program to find out the 'WHO region, 'Country', 'Beverage Types' in
 the year '1986' or '1989' where WHO region is 'Americas' or 'Europe' from
   the world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[((a["Year"]=="1986")|(a["Year"]==1989))
  &((a["WHO region"]=="Americas")|(a["WHO region"]=="Europe"))])&(a["Country"]) & (a["Beverage Types"])