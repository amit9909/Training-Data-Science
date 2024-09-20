import matplotlib.pyplot as mt
import pandas as pd
import numpy as np
x=np.array([2,3,4,5,6,7])
y=[4,5,6,8,9,8]
mt.plot(x,y)
mt.annotate("python",xy=(5,8),xytext=(4,8),arrowprops={"facecolor":"r"})
mt.show()