# Function dropna(), it removes the row which has any nan values.
import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.dropna()
print(a)


# Function fillna(), it adds the specific value you want to add on empty spaces of nan values.
import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.fillna(0)
print(a)

#do without using a function

import pandas as pd
a=pd.read_excel("check.xlsx")
a=a.fillna(0)
a["total"]=a["c"]+a["java"]+a["python"]
print(a)
