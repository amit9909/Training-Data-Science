"""write a pandas prgrm to remove the duplicates from 'who region' column of world
alcohol consumption dataset"""

import pandas as pd
a=pd.read_excel("ques1.xlsx")
a=a.drop_duplicates("who region")
print(a)