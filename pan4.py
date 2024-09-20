import pandas as pd
dic={"amit":[45,23,67],"aman":[65,56,67],"sonu":[45,87,98]}
x=pd.DataFrame(dic,index=["c","c++","python"])
print(x.loc[["c","python"]])