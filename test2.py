import pandas as pd
x= pd.DataFrame({'student_id': ['S1', 'S2', 'S3'],
                              'name': ['Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
                                                  'marks': [200, 210, 190,]}) 
y= pd.DataFrame({'student_id': ['S4', 'S5', 'S6'],
                            'name': ['Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
                            'marks': [201, 200, 198]}) 
print("Original DataFrames:") 
print(x) 
print(y) 
merged_data = pd.merge(x,y, on='student_id', how='inner')
print("Merged data (inner join):") 
print(merged_data)