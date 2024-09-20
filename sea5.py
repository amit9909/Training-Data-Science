import matplotlib.pyplot as mt
import seaborn as s
import pandas as pd
dat=s.load_dataset("penguins")
# s.barplot(x="island",y="bill_length_mm",data=dat,hue="sex",
#           hue_order=["Female","Male"],color="yellow",orient="v",
#           saturation=0.1,dodge=False,errcolor="red",errwidth=1,
#           capsize=0.4,palette="Accent")
mt.figure(figsize=(12, 8))
mt.subplot(1,2,1)
s.barplot(x="island",y="bill_length_mm",data=dat)
mt.subplot(1,2,2)
s.barplot(x="species",y="bill_length_mm",data=dat)
mt.show()
