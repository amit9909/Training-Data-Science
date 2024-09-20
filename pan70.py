import pandas as pd
import matplotlib.pyplot as mt
a={ "id":[1,2],
    "name": ["aman","ayushi"],
     "qualification":["mtech","btech"],
      "date":[2024,2022]
}

c=pd.DataFrame(a)
c.plot(x="id",y="date")
mt.show()
