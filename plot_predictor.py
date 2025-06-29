import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
numbers = df["numbers"].values
plt.hist(numbers, bins=4)
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.title("График чисел из data.csv")
plt.show()