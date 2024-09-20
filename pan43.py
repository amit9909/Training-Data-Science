"""write a pandas program to find out the alcohol consumption details in the year '1986'
  or '1989' where who region is 'Americas' or 'Europe'
    from the world alcohol consumptionn dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[((a["Year"]=="1986")|(a["Year"]==1989))
            &((a["WHO region"]=="Americas")|(a["WHO region"]=="Europe"))])
