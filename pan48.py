"""16. Write a Pandas program to filter those records where WHO region
 contains "Ea" substring from world alcohol consumption dataset"""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a[a["WHO region"].str.contains("Ea")])
