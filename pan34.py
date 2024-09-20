# write a program without fuction find the total when nan value is present in excel sheet

import pandas as pd
p=pd.read_excel("check.xlsx")
a=pd.DataFrame(p)

for i in a.columns:
    a.loc[a[i].isna(),i]=0

for i ,j in a.iterrows():
    for k in range(len(j)):
        x=str(a.iloc[i,k]).lower()=="nan"
        if x:
            a.iloc[i,k]=0
print(a)