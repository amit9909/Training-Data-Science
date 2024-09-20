"""write a pandas program to find out the alcohol 
consumption of a given year from the world
   alcohol consupmtion dataset"""

import pandas as pd
a=pd.read_excel("ques1.xlsx")
num=int(input("enter the year :"))
print(a.loc[(a["year"]==num)])