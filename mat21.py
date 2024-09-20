# import matplotlib.pyplot as mt
# import pandas as pd
# x=[2,3,4,5,6,7]
# y=[4,5,6,8,9,8]
# mt.plot(x,y)
# mt.fill_between(x,y)
# mt.show()

# import matplotlib.pyplot as mt
# import pandas as pd
# x=[2,3,4,5,6,7]
# y=[4,5,6,8,9,8]
# mt.plot(x,y)
# mt.fill_between(x=[2,3],y2=4,y1=6)
# mt.show()
# import matplotlib.pyplot as mt
# import pandas as pd
# import numpy as np
# x=np.array([2,3,4,5,6,7])
# y=[4,5,6,8,9,8]
# mt.plot(x,y)
# mt.fill_between(x,y,color="r",where=(x>4))
# mt.show()

# import matplotlib.pyplot as mt
# import pandas as pd
# import numpy as np
# x=np.array([2,3,4,5,6,7])
# y=[4,5,6,8,9,8]
# mt.plot(x,y)
# mt.fill_between(x,y,color="r",where=(x>4)&(x<=6))
# mt.show()


# import matplotlib.pyplot as mt
# import pandas as pd
# import numpy as np
# x=np.array([2,3,4,5,6,7])
# y=[4,5,6,8,9,8]
# mt.plot(x,y)
# mt.text(4,8,s="amit",style="italic")
# mt.show()

import matplotlib.pyplot as mt
import pandas as pd
import numpy as np
x=np.array([2,3,4,5,6,7])
y=[4,5,6,8,9,8]
mt.plot(x,y)
mt.text(4,8,s="amit",style="italic",bbox={"facecolor":"g"})
mt.show()