# Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}, удалить из него первый и последний элементы. Отобразить исходный
# и получившийся словарь. Использовать for, range.

dict1 = {}
for i in range(7):
    dict1[i] = i ** 3
print('Исходный:',dict1)
dict2 = dict1.copy()
dict2.pop(0)  
dict2.pop(6)
print("Получившийся:",dict2)