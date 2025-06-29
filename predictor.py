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
x4 = get_number("Введите четвертое число: ")
multiplier = get_number("Введите коэффициент (например, 2 для удвоения): ")
# Создаём массив из введённых чисел
X = np.array([x1, x2, x3, x4])

# Предсказание: сумма чисел с использованием NumPy
prediction = np.mean(X) * multiplier
print(f"Среднее значение чисел: {np.mean(X)}")
# Вывод результата
print(f"Предсказанное число: {prediction}")