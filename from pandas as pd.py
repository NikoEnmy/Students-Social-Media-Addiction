import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
file_path = 'C://Users//nikol//OneDrive//Документы//Students Social Media Addiction.csv'
data = pd.read_csv(file_path)
x = data['Mental_Health_Score']
y = data['Addicted_Score']
slope, intercept, r_value, p_value, std_err = linregress(x, y)

plt.scatter(x, y, alpha = 0.5, c='green')
plt.plot(x, slope * x + intercept, color='red', label=f'y={slope:.2f}x +{intercept:.2f}, r={r_value:.2f}')
plt.title('Addiction of level of addiction on mental health')
plt.xlabel("Mental Health Score")
plt.ylabel("Addicted Score")
plt.grid(True)
plt.legend()
plt.show()

print(f"Coefficient correlation: {r_value}")