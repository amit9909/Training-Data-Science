import pandas as pd
a=[23,67]
b=pd.Series(a)
b=b.to_frame()
print(b)


import pandas as pd
a=[23,67]
b=pd.Series(a)
b=b.to_frame("amit")
print(b)