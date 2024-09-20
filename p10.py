# import numpy as n
# a=n.array([[5,14],[6,8]])
# b=n.array([[10,11],[15,14]])
# c=n.array([[15,14],[18,16]])
# d=n.vstack((a,b))
# print(d)

# hstack and vstack did not need to define axis 
# import numpy as n
# a=n.array([[5,14],[6,8]])
# b=n.array([[10,11],[15,14]])
# c=n.array([[15,14],[18,16]])
# e=n.hstack((b,c))
# print(e)

# isme ek dimension badh jaayega valid to 3d only
import numpy as n
a=n.array([[5,7,8],[6,7,8]])
b=n.array([[8,7,6],[7,8,9]])
c=n.dstack((a,b))
print(c)
