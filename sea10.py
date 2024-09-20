import matplotlib.pyplot as mt
import seaborn as s
import numpy as np
import pandas as pd
a=pd.read_excel("sea.xlsx")
b=a.loc[(a["sex"]=="M")]
c=a.loc[(a["sex"]=="F")]


mt.show()