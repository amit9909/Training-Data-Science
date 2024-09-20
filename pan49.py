""""Write a Pandas program to filter those records where WHO region matches with multiple values
 (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset."""

import pandas as pd
a=pd.read_csv("kumar.csv")
print(a.loc[(a["WHO region"]=="Africa")|((a["WHO region"]=="Eastern Mediterranean")
            |(a["WHO region"]=="Europe"))])