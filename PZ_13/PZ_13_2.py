# В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import random
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for a in matrix:
    print(a)

n = len(matrix)
result = list(map(
    lambda i: list(map(
        lambda j: matrix[i][j] if i == j else matrix[i][j] * 2,
        range(n))),
    range(n)))
print("Получившаяся матрица:")
for b in result:
    print(b)