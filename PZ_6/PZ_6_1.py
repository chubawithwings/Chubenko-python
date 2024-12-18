#Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся в списке,
#на исходное значение первого четного числа.Если четные числа в списке отсутствуют,
#то оставить список без изменений.

def spisok(numbers):
    first_even = None
    for num in numbers:
        if num % 2 == 0:
            first_even = num
            break

    if first_even is None:
        return numbers

    modified_numbers = numbers[:]

    for i, num in enumerate(modified_numbers):
        if num % 2 == 0:
            modified_numbers[i] += first_even
    return modified_numbers
list = [1, 2, 3, 6, 8, 5, 10, 12]
result = spisok(list)
print(f"Исходный список: {list}, Измененный список: {result}")