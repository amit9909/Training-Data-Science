import pandas as pd
print(pd.__version__)


import pandas as pd
l=[87,45,67,87,34]
print(pd.Series(l))



# if u want to decide the value of indexing 

import pandas as pd
l=[87,45,67,89]
u=pd.Series(l,index=["aman","anjali","aashvee","amit"])
print(u)

#for specific value to access by using indexing 
import pandas as pd
l=[87,45,67,89]
u=pd.Series(l,index=["aman","anjali","aashvee","amit"])
print(u["amit"])