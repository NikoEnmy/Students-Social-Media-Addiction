import numpy as np

# Функция для безопасного ввода чисел
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число!")

# Ввод трёх чисел с проверкой
x1 = get_number("Введите первое число: ")
x2 = get_number("Введите второе число: ")
x3 = get_number("Введите третье число: ")

# Создаём массив из введённых чисел
X = np.array([x1, x2, x3])

# Предсказание: сумма чисел с использованием NumPy
prediction = np.sum(X)

# Вывод результата
print(f"Предсказанное число: {prediction}")