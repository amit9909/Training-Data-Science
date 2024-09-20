
import pandas as pd
import matplotlib.pyplot as mt

a=pd.read_csv("akv.csv")
b= a.pivot(index='Month', columns='Product', values='Sales')
mt.figure(figsize=(12, 8))
for product in b.columns:
    mt.plot(b.index,b[product], marker='o', label=product)

mt.show()


