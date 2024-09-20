import matplotlib.pyplot as mt
import pandas as pd
x=["c","python","node.js"]
y=[20,35,45]
mt.subplot(2,2,4)
mt.bar(x,y)
mt.subplot(2,2,2)
mt.scatter(x,y)
mt.subplot(2,2,3)
mt.pie(y,labels=x)
mt.subplot(2,2,1)
mt.plot(x,y)
mt.show()