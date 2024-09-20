import matplotlib.pyplot as mt
import pandas as pd
x=pd.read_csv("class.csv")
math=x["math"]
c=x["c"]
python=x["python"]
name=x["name"]
mt.subplot(1,3,1)
mt.plot(name,math)
mt.subplot(1,3,2)
mt.plot(name,python)
mt.subplot(1,3,3)
mt.plot(name,c)
mt.suptitle("class B")
mt.show()