#delete column 
import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.fillna(0)
a["percentage"]=(a["c"]+a["java"]+a["python"])/3
print(a)
print("*********************")
a=a.drop(["percentage"],axis=1)
print(a)


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


#dlete row specific
import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.fillna(0)
a["percentage"]=(a["c"]+a["java"]+a["python"])/3
print(a)
print("*********************")
a=a.drop(index=2,axis=0)
print(a)