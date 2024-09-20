
import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.fillna(0)
a["percentage"]=(a["c"]+a["java"]+a["python"])/3
a.loc[(a["percentage"]>90),["Grade"]]="A"
a.loc[(a["percentage"]>=80)& (a["percentage"]<=90),["Grade"]]="B"
a.loc[(a["percentage"]>=60)& (a["percentage"]<80),["Grade"]]="C"
a.loc[(a["percentage"]>=50)& (a["percentage"]<60),["Grade"]]="D"
a.loc[(a["percentage"]>=33)& (a["percentage"]<50),["Grade"]]="E"
a.loc[(a["percentage"]<33),["Grade"]]="F"
print(a)