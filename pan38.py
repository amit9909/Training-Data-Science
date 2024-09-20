"""write a pandas program to find out the alcohol consumption details in the year
   '1987' or '1989' from the world alcohol consumption dataset"""

import pandas as pd
a=pd.read_excel("ques1.xlsx")
print(a.loc[(a["year"]==1987) | (a["year"]==1989)])