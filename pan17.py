'''import pandas as pd
a=pd.read_csv("amit.csv")
print(a.head(20))
print(a.tail(20))
print(a.info(20))'''



#print specific column

import pandas as pd
a=pd.read_csv("amit.csv")
print(a["kumar"])



import pandas as pd
a=pd.read_csv("amit.csv")
print(a["kumar"].head())