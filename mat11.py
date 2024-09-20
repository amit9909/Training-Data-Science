import matplotlib.pyplot as mt
import pandas as pd
sub="c"
sem1=pd.read_excel("sem.xlsx",sheet_name="sem1").loc[:,["name",sub]]
sem2=pd.read_excel("sem.xlsx",sheet_name="sem2").loc[:,["name",sub]]
sem3=pd.read_excel("sem.xlsx",sheet_name="sem3").loc[:,["name",sub]]
sem1["total"]=sem1[sub]+sem2[sub]+sem3[sub]
print(sem1)
sem1=(sem1.sort_values("total"))
print(sem1)
sem1=sem1.reset_index()
x=[0,"sem1","sem2","sem3"]
failure=sem1.loc[0]["name"]
topper=sem1.loc[len(sem1["name"])-1]["name"]
print(f"failure is:",failure,"\n" f"topper is :",topper)

y=[0,sem1.loc[(sem1["name"]==topper)][sub].values[0],
   sem2.loc[(sem1["name"]==topper)][sub].values[0],
   sem3.loc[(sem1["name"]==topper)][sub].values[0]]

y1=[0,sem1.loc[(sem1["name"]==failure)][sub].values[0],
   sem2.loc[(sem1["name"]==failure)][sub].values[0]
   ,sem3.loc[(sem1["name"]==failure)][sub].values[0]]

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
    
mt.show()


    














   

