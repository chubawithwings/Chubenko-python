# В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import random
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]

print("Исходная матрица:")
for a in matrix:
    print(a)

for i in range(4):
    for j in range(4):
        if i != j:
            matrix[i][j] *= 2

print("Полученная матрица:")
for a in matrix:
    print(a)
