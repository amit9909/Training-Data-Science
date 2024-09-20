import pandas as pd
a=pd.read_excel("amit.xlsx")
a["total"]=a["math"]+a["chemistry"]+a["physics"]
a["percentage"]=a["total"]/3
print(a)




