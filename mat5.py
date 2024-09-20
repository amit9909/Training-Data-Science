import matplotlib.pyplot as mt
import pandas as pd
a=pd.read_csv("class.csv")
a["percentage"]=(a["math"]+a["python"]+a["c"])/3
name=a["name"]
percentage=a["percentage"]
a.loc[(a["percentage"]>90),["Grade"]]="A"
a.loc[(a["percentage"]>=80),["Grade"]]="B"
a.loc[(a["percentage"]>=60),["Grade"]]="C"
a.loc[(a["percentage"]>=50),["Grade"]]="D"
a.loc[(a["percentage"]>=33),["Grade"]]="E"
a.loc[(a["percentage"]<33),["Grade"]]="F"
mt.plot(name,percentage)
mt.xlabel("name")
mt.ylabel("percentage")
mt.title("class information")
mt.show()