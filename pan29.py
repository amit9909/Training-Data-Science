#print whose total is greater than 90
import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.loc[(a["python"]>50) & (a["java"]>70)])
