
import pandas as pd
a=pd.read_excel("check.xlsx")
a["percentage"]=(a["c"]+a["java"]+a["python"])/3
a.loc[(a["percentage"]>50),["Grade"]]="A"
print(a)
