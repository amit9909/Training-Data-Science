"""21. Write a Pandas program to filter 
rows based on row numbers ended with 0, like 0, 10, 20, 30
 from world alcohol consumption dataset."""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a.index%10==0)])


########## 2nd method

import pandas as pd
a=pd.read_csv("kumar.csv")
for i,j in a.iterrows():
    if i%10==0:
        print(a.loc[i])

