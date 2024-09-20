#pehla row alg ho jaayega aur doosra bhi in vsplit
import numpy as n
a=n.array([[5,4,6],[1,2,3]])
c=n.vsplit(a,2)
print(c)


import numpy as n
a=n.array([[5,4,6],[1,2,3]])
c=n.hsplit(a,3)
print(c)