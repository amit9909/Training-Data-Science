import matplotlib.pyplot as mt
import pandas as pd
sem1=pd.read_excel("topper.xlsx",sheet_name="Sheet1")
sem2=pd.read_excel("topper.xlsx",sheet_name="Sheet2")
sem3=pd.read_excel("topper.xlsx",sheet_name="Sheet3")
sem1["total"]=sem1["c"]+sem1["python"]
print(sem1)
sem2["total"]=sem2["c"]+sem2["python"]
print(sem2)
sem3["total"]=sem3["c"]+sem3["python"]
print(sem3)
total=sem1["total"]+sem2["total"]+sem3["total"]
sem1=(sem1.sort_values("total"))
sem1=sem1.reset_index()
print(sem1)
x=[0,"sem1","sem2","sem3"]

topper=sem1.loc[len(sem1["name"])-1]["name"]


y=[0,sem1.loc[(sem1["name"]==topper)]["c"].values[0],
   sem2.loc[(sem1["name"]==topper)]["c"].values[0],
   sem3.loc[(sem1["name"]==topper)]["c"].values[0]]


y1=[0,sem1.loc[(sem1["name"]==topper)]["python"].values[0],
   sem2.loc[(sem1["name"]==topper)]["python"].values[0],
   sem3.loc[(sem1["name"]==topper)]["python"].values[0]]

print(y,y1)

for i in range(len(x)-1):
     
    if y[i]<y[i+1]:
        mt.plot(x[i:i+2],y[i:i+2],color="green")
    elif y[i]>y[i+1]:
       
        mt.plot(x[i:i+2],y[i:i+2],color="red")
    else:
        
        mt.plot(x[i:i+2],y[i:i+2],color="yellow")

    if y1[i]<y1[i+1]:
        mt.plot(x[i:i+2],y1[i:i+2],color="green")
    elif y1[i]>y1[i+1]:
       
        mt.plot(x[i:i+2],y1[i:i+2],color="red")
    else:
        
        mt.plot(x[i:i+2],y1[i:i+2],color="yellow")
mt.legend()
mt.title(topper)
mt.show()


