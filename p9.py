'''import numpy as n
a=n.array([[5,7,8],[6,7,8]])
b=n.array([[8,7,6],[7,8,9]])
c=n.concatenate((a,b),axis=0)
print(c)



import numpy as n
a=n.array([[[5,7,8],[6,7,8]]])
b=n.array([[[8,7,6],[7,8,9]]])
c=n.concatenate((a,b),axis=0)
print(c)
#stack mein ek dimension badh jaayega 
import numpy as n
a=n.array([[5,7,8],[6,7,8]])
b=n.array([[8,7,6],[7,8,9]])
c=n.stack((a,b))
print(c)'''

import numpy as n
a=n.array([[5,7,8],[6,7,8]])
b=n.array([[8,7,6],[7,8,9]])
c=n.stack((a,b),axis=1)
print(c)

#axis 0 for column and axis =1 for row