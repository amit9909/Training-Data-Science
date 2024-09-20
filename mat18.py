import matplotlib.pyplot as mt
import pandas as pd
name="amit"
data=pd.read_excel("pie.xlsx")
data=data.loc[data["name"]==name]
total=data["c"]+data["python"]+data["pandas"]+data["numpy"]
sub1=(data["c"]/total)*100
sub2=(data["python"]/total)*100
sub3=(data["pandas"]/total)*100
sub4=(data["numpy"]/total)*100
print(sub1,sub2,sub3,sub4)
z=[0,0,0,0]
x=[sub1.values[0],sub2.values[0],sub3.values[0],sub4.values[0]]
i=x.index(max(x))
z[i]=0.1
y=["c","python","pandas","numpy"]
mt.pie(x,labels=y,explode=z)
mt.show()