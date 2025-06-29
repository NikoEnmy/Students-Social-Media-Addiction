import pandas as pd
import matplotlib.pyplot as plt
file_path = 'C://Users//nikol//OneDrive//Документы//Students Social Media Addiction.csv'
data = pd.read_csv(file_path)
avg_by_gender = data.groupby('Gender')['Addicted_Score'].mean()
print("Average level of addiction by gender:")
print(avg_by_gender)

avg_by_age = data.groupby('Age')['Addicted_Score'].mean()
avg_by_age.plot(kind='line', marker='o')
plt.title('level of addiction by age')
plt.xlabel('Age')
plt.ylabel('Addicted Score')
plt.grid(True)
plt.show()