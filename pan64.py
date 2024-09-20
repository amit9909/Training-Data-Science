import pandas as pd
a={ "id":[1,2],
    "name": ["aman","ayushi"],
     "qualification":["mtech","btech"],
      "date":[2024,2022]
}
b={ "id":[1,3],
    "name": ["aman","rashmi"],
     "qualification":["mtech","btech"],
      "salary":[45000,30000]
}
c=pd.DataFrame(a)
d=pd.DataFrame(b)
e=pd.merge(c,d)
print(e)