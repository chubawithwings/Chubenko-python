# Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.

import random
matrix1 = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
matrix2 = [[0 if num > 10 else num for num in row] for row in matrix1]
print("Исходная матрица:")
for row in matrix1:
    print(row)

print("Полученная матрица:")
for row in matrix2:
    print(row)
