import pandas as pd
x=pd.read_csv("hello.csv")
sub=input("Enter Subject :")
max=x[sub].max()
print(f"Topper of {sub} is {x['name'][x[sub]==max]}")