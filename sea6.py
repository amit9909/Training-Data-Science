import matplotlib.pyplot as mt
import seaborn as s
import pandas as pd
dat=s.load_dataset("tips")
s.scatterplot(x="total_bill",y="tip",
              data=dat,
              hue="sex",
              palette="Oranges",
              style="sex",
              markers={"Female":"D","Male":"*"},
              sizes=(100,160))
mt.show()
