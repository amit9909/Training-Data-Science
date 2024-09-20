"""import matplotlib.pyplot as mt
import pandas as pd
x=["c","python","node.js"]
y=[20,35,45]
mt.pie(y,labels=x)
mt.legend(title="coding languages",loc=("upper left"))
mt.show()"""


import matplotlib.pyplot as mt
import pandas as pd
x=["c","python","node.js"]
y=[20,35,45]
z=[0,0,2]
c=["r","b","g"]
mt.pie(y,
       labels=x,
        explode=z,
       shadow=True,
       labeldistance=0.2,
       counterclock=True,
       rotatelabels=True,
       textprops={"fontsize":15,"color":"red"},
        colors=c)
mt.legend(title="coding languages",loc=("upper left"))
mt.show()