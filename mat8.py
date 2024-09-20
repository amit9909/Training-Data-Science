import matplotlib.pyplot as mt
import pandas as pd
x=pd.read_excel("btech.xlsx",sheet_name="Sheet1")
y=pd.read_excel("btech.xlsx",sheet_name="Sheet2")
z=pd.read_excel("btech.xlsx",sheet_name="Sheet3")

sub=input("enter subject : ")
mt.subplot(1,3,1)
mt.plot(x["name"],x[sub])
mt.xlabel("name")
mt.ylabel("Marks")
mt.title("Display marks")

mt.subplot(1,3,2)
mt.plot(y["name"],y[sub])
mt.xlabel("name")
mt.ylabel("Marks")
mt.title("Display marks")

mt.subplot(1,3,3)
mt.plot(z["name"],z[sub])

mt.xlabel("name")
mt.ylabel("Marks")
mt.title("Display marks")

mt.suptitle("B.Tech")

mt.show()
