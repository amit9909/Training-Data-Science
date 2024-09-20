"""27. Write a Pandas program to
 filter all records starting from the 2nd row, 
 access every 5th row from world alcohol consumption dataset"""


import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[2::5])