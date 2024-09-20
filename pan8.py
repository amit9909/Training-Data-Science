#make a pandas dataframe with a two dimesnional list
import pandas as pd
l=[[2,3,4],[34,55,67]]
x=pd.DataFrame(l)
print(x)



import pandas as pd
l=[[2,3],[34,55]]
x=pd.DataFrame(l,columns=["aman","amit"])
print(x)