import matplotlib.pyplot as mt
import pandas as pd
x=[45,54,85,65,85]
y=[13,42,54,75,87]
mt.scatter(x,y,c=y,cmap="Oranges")
mt.colorbar()
mt.show()