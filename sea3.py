import matplotlib.pyplot as mt
import seaborn as s
import pandas as pd
dat=pd.read_csv("flights.csv")
s.lineplot(x="month",y="passengers",data=dat)
mt.show()