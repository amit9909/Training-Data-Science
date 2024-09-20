#small values dark and largest values light
import matplotlib.pyplot as mt
import pandas as pd
import numpy as np
x=np.array([2,3,4,5,6,7])
y=[4,5,6,8,9,8]
mt.scatter(x,y,cmap="Blues_r",c=y)
mt.show()