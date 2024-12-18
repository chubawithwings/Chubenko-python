# Составить функцию, которая выполнит суммирования числового ряда

def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = 20
result = sum_of_series(n)
print(f"Сумма чисел от 1 до {n} равна {result}")

