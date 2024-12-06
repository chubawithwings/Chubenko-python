def day_of_week(k):
    # Определяем номер дня недели
    day = (4 + k - 1) % 7  # 4 - четверг
    return day

k = int(input("Введите номер дня года (от 1 до 365): "))

# Вычисление и вывод результата
if 1 <= k <= 365:
    print(f"Номер дня недели для {k}-го дня года: {day_of_week(k)}")
else:
    print("Ошибка: Введите число от 1 до 365.")
