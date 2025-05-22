# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной 
# последовательности из целых положительных и отрицательных чисел. Сформировать новый текстовый 
# файл (.txt) следующего вида, предварительно выполнив требусмую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Индекс первого минимально элемента первого файла:
# Индекс последнего максимального элемента второго файла:
# Элементы кратные 4 первого и второго файлов:

l1 = '-1 2 -6 35 44 -83 25 -48'
l2 = '5 -98 -9 -3 255 -3 46 28'
f1 = open ('f1.txt','w')
f1.writelines(l1)
f1.close()
f2 = open ('f2.txt','w')
f2.writelines(l2)
f2.close()

f3 = open('f3', 'w')
f3.write('Элементы первого и второго списков:')
f3.write('/n')
f3.writelines(l1)
f3.write('/n')
f3.writelines(l2)
f3.close()

f1 = open('f1.txt')
k1 = f1.read()
a1 = k1.split()
for i in range(len(a1)):
    a1[i] = int(a1[i])
f1.close()

f2 = open('f2.txt')
k2 = f2.read()
a2 = k2.split()
for i in range(len(a2)):
    a2[i] = int(a2[i])
f2.close()

f1 = open('f1.txt')
f2 = open('f2.txt')
a1_l = list(a1)
f1_index = a1_l.index(min(a1_l))
a2_l = list(a2)
f2_index = a2_l.index(max(a2_l))
kratn = []
for i in a1_l:
    if i % 4 == 0:
        kratn.append(i)
for d in a2_l:
    if d % 4 == 0:
        kratn.append(d)
f1.close()
f2.close()

f3 = open('f3','a')
f3.write('/n')
print('Количество элементов первого и второго файлов: ', len(a1 + a2), ', Индекс первого минимально элемента первого файла:', f1_index, file=f3)
print('Индекс последнего максимального элемента второго файла:', f2_index, ', Элементы кратные 4 первого и второго файлов:', kratn, file=f3)
f3.close()
f3 = open('f3','r')
print(f3.read())
f3.close()