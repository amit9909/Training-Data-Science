import matplotlib.pyplot as mt
import seaborn as s
# print(s.__version__)
import pandas as pd
x=[10,20,30]
y=[20,60,10]
dat=pd.DataFrame({"time":x,"speed":y})
s.lineplot(x="time",y="speed",data=dat)
mt.show()
