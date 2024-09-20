import pandas as pd
a=pd.read_excel("ques1.xlsx")
print(a)
print(a["country beverage"])
print(a["year"])
print(a.iloc[0:2,1:5]) 
print(a.iloc[0:6,1:3]) 
#or
print(a.head(2))



#write a pandas program to select random number of rows ,fraction of random rows from
#worlddd alcohol consumption dataset.

import pandas as pd
import numpy as np
a=pd.read_excel("ques1.xlsx")
x=np.random.radint(1,len(a)+1)
y=a.simple(n=x)
print(y)