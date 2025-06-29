import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
file_path = 'C://Users//nikol//OneDrive//Документы//Students Social Media Addiction.csv'
data = pd.read_csv(file_path)
data['Age_Group'] = pd.cut(data['Age'], bins=[17, 20, 24], labels=['18,20', "21-24"])
avg_by_age_group = data.groupby('Age_Group')["Addicted_Score"].mean()
avg_by_age_group.plot(kind="bar", color="orange")
plt.title("Average level of addiction by age group")
plt.xlabel("Age group")
plt.ylabel("Addicted Score")
plt.show()