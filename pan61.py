import pandas as pd
a=pd.read_excel("college.xlsx")
a1=pd.DataFrame(a)
b=pd.read_excel("school.xlsx")
b1=pd.DataFrame(b)
e=pd.concat([a1,b1],axis=1,join="inner")
print(e.loc[((a1["percentage"]>70)&(b1["percentage"]>75)),"name"].iloc[:,0:1])