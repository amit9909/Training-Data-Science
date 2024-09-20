import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
 
df = pd.DataFrame({ 'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,
                              70010,70003,70012,np.nan,70013],
                                'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,
                                             2480.4,250.45, 75.29,3045] })
print("Original Orders DataFrame:") 
print(df)
print("\nNumber of missing values of the said dataframe:")
print(df.isna().sum())