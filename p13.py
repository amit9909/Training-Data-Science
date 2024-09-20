
import numpy as n
a=n.array([[5,4,6],[1,2,3]])
c=n.sort(a)
print(c)



import numpy as n
a=n.array([1,2,4,6,9,56])
c=n.searchsorted(a,4)
print(c)



import numpy as n
a=n.array([1,2,4,6,9,56])
c=n.searchsorted(a,4,side="right")
print(c)