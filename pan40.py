"""write a pandas program to find out the alcohol consumption details
 by the 'americas' in the year '1986' 
   from the world consumption dataset """

import pandas as pd
a=pd.read_excel("ques1.xlsx")
print(a.loc[(a["who region"]=="Americas") & (a["year"]==1986)])