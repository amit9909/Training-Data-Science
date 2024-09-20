import matplotlib.pyplot as mt
import pandas as pd
a=pd.read_excel("teach.xlsx",sheet_name="secA")
b=pd.read_excel("teach.xlsx",sheet_name="secB")
t1=(a["t1"].sum()+b["t1"].sum())/2
t2=(a["t2"].sum()+b["t2"].sum())/2
t3=(a["t3"].sum()+b["t3"].sum())/2
x=[t1,t2,t3]
print(x)
z=[0,0,0]
i=x.index(max(x))
z[i]=0.2
mt.pie(x,labels=["t1","t2","t3"],autopct="%0.1f%%",explode=z)
mt.show()

