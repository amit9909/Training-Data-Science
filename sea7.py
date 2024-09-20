import matplotlib.pyplot as mt
import seaborn as s
import pandas as pd
a=s.load_dataset("penguins")
s.displot(a["bill_length_mm"],
          bins=[30,35,40,45,50,55,60]
          ,kde=True
          ,rug=True,
          color="red"
          )
mt.show()