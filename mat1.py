'''import matplotlib.pyplot as mt
import numpy as np
a=np.array([2,5])
b=np.array([4,6])
mt.plot(a,b)
mt.show()'''



"""import matplotlib.pyplot as mt
import numpy as np
a=np.array([2,7,7,8,7])
b=np.array([9,6,7,9,7])
mt.plot(a,b)
mt.show()"""


#using marker
"""import matplotlib.pyplot as mt
import numpy as np
a=np.array([2,7,7,8,7])
b=np.array([9,6,7,9,7])
mt.plot(b,marker="|")
mt.show()"""

"""#using color
import matplotlib.pyplot as mt
import numpy as np
a=np.array([2,7,7,8,7])
b=np.array([9,6,7,9,7])
mt.plot(b,marker="d",color="g")
mt.plot(a,marker="*",color="r")
mt.show()"""

#change the style of a line

import matplotlib.pyplot as mt
import numpy as np

a=[int(input(f"enter your marks of maths , c, python ,fullstack :"))for i in range(len())]
b=[int(input(f"enter your marks of maths , c, python ,fullstack :"))for i in range(len())]
c=[int(input(f"enter your marks of maths , c, python ,fullstack :"))for i in range(len())]

mt.plot(a,b,c)
mt.show()