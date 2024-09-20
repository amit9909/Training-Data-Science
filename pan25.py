import pandas as pd
a=pd.read_excel("amit.xlsx")
a["percentage"]=0
total=0
toppername=""
for i,j in a.iterrows():
    if total<j["math"]+j["chemistry"]+j["physics"]:
        total=j["math"]+j["chemistry"]+j["physics"]
        toppername=j["name"]
print("class of topper is ",toppername)
percentage=total/3
print(percentage)
