
import pandas as pd
a=pd.read_csv("amit.csv")
for i,j in a.iterrows():
    print(i,j["kumar"])
print(a["amit"].max())



#without function
import pandas as pd
a=pd.read_csv("amit.csv")
for i,j in a.iterrows():
    if max<j["kumar"]:
        max=j["kumar"]
print(a[a["kumar"]==max].head(1))
