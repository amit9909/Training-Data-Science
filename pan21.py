import pandas as pd
a=pd.read_csv("hello.csv")
total=0
toppername=""
for i,j in a.iterrows():
    if total<j["math"]+j["c"]+j["python"]:
        total=j["math"]+j["c"]+j["python"]
        toppername=j["name"]
print("class of topper is ",toppername)