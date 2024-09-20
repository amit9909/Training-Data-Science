#split fumction is valid if the elemnts are same for dividing
# if elemets are less it is not divided array
import numpy as n
a=n.array([5,4,6,7,7,6,8,5])
c=n.split(a,2)
print(c)

#it works for any elemnts in array to divide the array
import numpy as n
a=n.array([5,4,6,7,7,6,8])
c=n.array_split(a,2)
print(c)

import numpy as n
a=n.array([5,4,6,7,7])
c=n.array_split(a,4)
print(c)