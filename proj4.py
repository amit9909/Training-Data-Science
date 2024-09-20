import matplotlib.pyplot as mt
import pandas as pd
import seaborn as s
read=pd.read_csv('mr.csv')
print(read.head())
read['Total']=read['MathScore']+read['ReadingScore']+read['WritingScore']
read['Average']=read['Total']/3
mt.figure(figsize=[10,5])
s.barplot(data=read,x='ParentEduc',y='Average',
          hue='Gender')
mt.title('Average Marks according to Parent Education')

mt.figure(figsize=[7,3])
s.barplot(data=read,x='EthnicGroup',y='Average',
          hue='Gender')
mt.title('Average Marks according to Ethinic Group')
mt.legend(loc=2)
mt.show()