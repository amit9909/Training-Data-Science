import matplotlib.pyplot as mt
import numpy as np
a=np.array([2,7,7,8,7])
b=np.array([9,6,7,9,7])
mt.xlabel("amit")
mt.ylabel("style")
mt.title("myself",loc="left")
mt.plot(a,b)
mt.grid(axis="y",color="r")
mt.legend()
mt.show()