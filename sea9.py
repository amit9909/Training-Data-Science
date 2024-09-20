import matplotlib.pyplot as mt
import seaborn as s
import numpy as np
import pandas as pd
a=s.load_dataset("tips")
s.pairplot(a,vars=["total_bill","tip"],hue="sex", hue_order=["Female","Male"])
mt.show()