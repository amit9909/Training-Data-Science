"""write a pandas program to find and drop the missing values from 
world alcohol consumption dataset."""
import pandas as pd
a=pd.read_excel("ques1.xlsx")
a=a.isna()
print(a)
a=a.dropna()
print(a)
