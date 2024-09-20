import matplotlib.pyplot as mt
import seaborn as s
import numpy as np
import pandas as pd
a=pd.read_csv("heart.csv")
#print(a.head())
#print(a.tail())
# print(a.info())
# print(a,"shape")
# print(a.dropna())
a=a.drop_duplicates()
# print(a.describe())
# print(a)
# b=a.loc[:,["id","age","oldpeak","ca","trestbps","chol","thalch","num"]]
# print(b)
# b=b.fillna(0)

# s.countplot(x=a["target"],data=a,hue="sex")
# s.histplot(x=a["target"],data=a,hue="sex")
# s.barplot(x=a["target"],y=a["cp"])
# s.barplot(x=a["target"],y=a["fbs"])
# s.histplot(x=a["restecg"],data=a,hue="sex")
s.pairplot(a)
mt.show()