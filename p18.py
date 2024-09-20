# filter
from numpy import array,random
a=array(random.randint(1,10,size=(2,5)))
print(a)
b=a[a>6]
print(b)