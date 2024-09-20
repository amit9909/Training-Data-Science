import pandas as pd
a=pd.read_excel("school.xlsx")
a1=pd.DataFrame(a)
b=pd.read_excel("college.xlsx")
b1=pd.DataFrame(b)
f= a1._append(b1)
print(f)
