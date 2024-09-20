from numpy import array,random
a=array(random.randint(1,10,size=(2,5)))
b=random.shuffle(a)
print(a)

from numpy import array,random
a=array(random.randint(1,10,size=(2,5)))
print(a)
b=random.permutation(a)
print(b)

