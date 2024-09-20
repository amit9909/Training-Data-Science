import matplotlib.pyplot as mt
import pandas as pd
a=pd.read_csv("class.csv")
name=a["name"]
percentage=a["percentage"]
mt.plot(name,percentage)
mt.xlabel("name")
mt.ylabel("percentage")
mt.title("class information")
mt.show()