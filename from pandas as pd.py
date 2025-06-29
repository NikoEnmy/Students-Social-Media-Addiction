import pandas as pd
import matplotlib.pyplot as plt
file_path = 'C://Users//nikol//OneDrive//Документы//Students Social Media Addiction.csv'
data = pd.read_csv(file_path)
correlation = data['Addicted_Score'].corr(data["Mental_Health_Score"])
print(f"Corelation between addiction and mental health: {correlation}")

plt.scatter(data["Mental_Health_Score"], data['Addicted_Score'], alpha=0.5, c="green")
plt.title('Addiction of level of addiction on mental health')
plt.xlabel('Mental Health Score')
plt.ylabel('Addicted Score')
plt.grid(True)
plt.show()