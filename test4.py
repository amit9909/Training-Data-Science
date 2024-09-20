
import pandas as pd
import matplotlib.pyplot as mt
a=pd.read_csv("akv.csv")
months = a["month_number"]
total_profits = a["total_profit"]
mt.figure(figsize=(10, 6))
mt.plot(months, total_profits, marker='o', linestyle='-', color='b')
mt.xlabel('Month Number')
mt.ylabel('Total Profit')
mt.title('Total Profit Over Months')
mt.grid(True)
mt.show()



   

