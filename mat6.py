import matplotlib.pyplot as mt
import pandas as pd
a=pd.read_csv("class.csv")
a["percentage"]=(a["math"]+a["python"]+a["c"])/3
name=a["name"]
percentage=a["percentage"]
sub=input("enter subject : ")
mt.plot(name,sub)
mt.xlabel("percentage")
mt.ylabel("name")
mt.title("class information")
mt.show()