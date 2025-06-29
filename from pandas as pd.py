import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
file_path = 'C://Users//nikol//OneDrive//Документы//Students Social Media Addiction.csv'
data = pd.read_csv(file_path)
avg_by_academic = data.groupby('Academic_Level')['Addicted_Score'].mean()
avg_by_academic.plot(kind="bar", color="skyblue")
plt.title("Average level of addiction by academic level")
plt.xlabel("Academic Level")
plt.ylabel("Addicted Score")
plt.show()

avg_by_relationship = data.groupby("Relationship_Status")["Addicted_Score"].mean()
avg_by_relationship.plot(kind='bar', color="lightgreen")
plt.title("Average level of addiction by relationship status")
plt.xlabel('Relationship Status')
plt.ylabel("Addicted Score")
plt.show()