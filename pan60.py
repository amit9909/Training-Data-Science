import pandas as pd
a={
    "name":["amit","ayushi"],
    "qualification":["Mtech","Btech"]
}
b={
    "name":["amit","Rashmi"],
    "qualification":["Mtech","Btech"]
}
c=pd.DataFrame(a)
d=pd.DataFrame(b)
e=pd.concat([c,d])
print(e)
f=([c,d].append)
print(f)
# c.to_csv('xyz.csv')
# c=pd.DataFrame(a,index=[1,2])
# d=pd.DataFrame(b,index=[1,3])
# e=pd.concat([c,d],axis=1,join="inner")
# print(e)