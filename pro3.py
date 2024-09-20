import numpy as  n
import pandas as p 
import matplotlib.pyplot as mt 
data=p.read_csv('mr.csv')
print(data.head())
print(data.tail())
print(data.isnull().sum())
data=data.fillna(0)
data['total']=(data['MathScore']+data['ReadingScore']+data['WritingScore'])/3
print(data)
education=(data["ParentEduc"].values)
new = set(education)
new = n.array(list(new))
high_school=data.loc[data['ParentEduc']=='high school']
master_degree=data.loc[data['ParentEduc']=="master's degree"]
some_college=data.loc[data['ParentEduc']=='some college']
associate_degree=data.loc[data['ParentEduc']=="associate's degree"]
some_high_school=data.loc[data['ParentEduc']=='some high school']
bachelor_degree=data.loc[data['ParentEduc']=="bachelor's degree"]

x=[high_school['total'].values[0],master_degree['total'].values[0],some_college['total'].values[0],associate_degree['total'].values[0],some_high_school['total'].values[0],bachelor_degree['total'].values[0]]
y=[0,0,0,0,0,0]
i=x.index(max(x))
y[i]=0.1
lable=['high school','master degree','some college degree','associate degree','some high school degree','bachelor degree']
mt.pie(x,explode=y,labels=lable)
mt.show()