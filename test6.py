import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("akv.csv")


pivot_df = df.pivot(index='"month_number', columns=["facecream" ,"facewash","toothpaste","bathingsoap" ,"shampoo","moisturizer"] )


plt.figure(figsize=(12, 8))
for product in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df["facecream" ,"facewash","toothpaste","bathingsoap" ,"shampoo","moisturizer"], marker='o', label=product)

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Data for Different Products')
plt.legend(title='Product')
plt.grid(True)
plt.show()