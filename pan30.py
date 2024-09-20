import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.loc[a["c"].isna()])
print()



import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.duplicated())
print()



import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.drop_duplicates())
print()



import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.sort_values("python"))
print()


import pandas as pd
a=pd.read_excel("check.xlsx")
print(a.sort_values("python")["python"])
print()