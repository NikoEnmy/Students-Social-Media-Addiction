import pandas as pd
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число!")
df = pd.read_csv("data.csv")
average = df["numbers"].mean()
multiplier = get_number("Введите коэффициент (например, 2 для удвоения): ")
prediction = average * multiplier 
print(f"Среднее значение чисел: {average}")
print(f"Предсказанное число: {prediction}")