import pandas as pd
x=pd.read_csv("hello.csv")
print(x["math"].max())
print(x["python"].max())
print(x["c"].max())
