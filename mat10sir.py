import matplotlib.pyplot as mt
import pandas as pd
x=pd.read_excel("sem.xlsx",sheet_name="sem1")
y=pd.read_excel("sem.xlsx",sheet_name="sem2")
z=pd.read_excel("sem.xlsx",sheet_name="sem3")
name=input("enter the student name")
sub=input("enter the subject name")
sem1mark=x.loc[x["name"]==name][sub].values[0]
sem2mark=y.loc[x["name"]==name][sub].values[0]
sem3mark=z.loc[x["name"]==name][sub].values[0]

a=[0,"x","y","z"]
b=[0,sem1mark,sem2mark,sem3mark]

for i in range(len(a)-1):
     
    if b[i]<b[i+1]:
        mt.plot(a[i:i+2],b[i:i+2],color="green")
    elif b[i]>b[i+1]:
       
        mt.plot(a[i:i+2],b[i:i+2],color="red")
    else:
        
        mt.plot(a[i:i+2],b[i:i+2],color="yellow")
mt.show()
    