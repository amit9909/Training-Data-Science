import pandas as pd
a=pd.read_excel("amit.xlsx")
a=pd.DataFrame(a)
print(a.loc[[3]])


import pandas as pd
a=pd.read_excel("amit.xlsx")
a=pd.DataFrame(a)
print(a.iloc[0,1])



import pandas as pd
a=pd.read_excel("amit.xlsx")
a=pd.DataFrame(a)
print(a.iloc[0,2])



#slicing using

import pandas as pd
a=pd.read_excel("amit.xlsx")
a=pd.DataFrame(a)
print(a.iloc[0:2,1:4])