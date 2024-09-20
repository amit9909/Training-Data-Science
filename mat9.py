import matplotlib.pyplot as mt
import pandas as pd
x=pd.read_excel("btech.xlsx",sheet_name="Sheet1")
y=pd.read_excel("btech.xlsx",sheet_name="Sheet2")
z=pd.read_excel("btech.xlsx",sheet_name="Sheet3")



sub=input("enter subject : ")
avg_1 = x[sub].sum()/x[sub].count()
avg_2 = y[sub].sum()/y[sub].count()
avg_3 = z[sub].sum()/z[sub].count()
b=max(avg_1,avg_2,avg_3)
c=min(avg_1,avg_2,avg_3) 

if avg_1==b:
 mt.subplot(1,3,1)
 mt.plot(x[sub],color="green")
 mt.title("Section A")


if avg_2==b:
 mt.subplot(1,3,2)
 mt.plot(x[sub],color="green")
 mt.title("Section B")

 
if avg_3==b:
 mt.subplot(1,3,3)
 mt.plot(x[sub],color="green")
 mt.title("Section C")

 
if avg_1==c:
 mt.subplot(1,3,1)
 mt.plot(x[sub],color="red")
 mt.title("Section A")
if avg_2==c:
 mt.subplot(1,3,2)
 mt.plot(x[sub],color="red")
 mt.title("Section B")
if avg_3==c:
 mt.subplot(1,3,3)
 mt.plot(x[sub],color="red")
 mt.title("Section C")

 if avg_1<b and avg_1>c:
  mt.subplot(1,3,1)
  mt.plot(x[sub],color="yellow")
  mt.title("Section A")

 if avg_2<b and avg_2>c:
  mt.subplot(1,3,2)
  mt.plot(x[sub],color="yellow")
  mt.title("Section B")
  
if avg_3<b and avg_3>c:
  mt.subplot(1,3,3)
  mt.plot(x[sub],color="yellow")
  mt.title("Section C")




mt.suptitle("B.Tech CSE DEPARTMENT")

mt.show()
