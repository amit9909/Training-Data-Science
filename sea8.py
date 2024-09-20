import matplotlib.pyplot as mt
import seaborn as s
import pandas as pd
a=s.load_dataset("tips")
s.countplot(x="sex",data=a,hue="smoker",palette="Accent",saturation=0.1)
mt.show()