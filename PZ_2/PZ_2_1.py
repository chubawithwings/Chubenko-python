def day_of_week(k):
    # Проверяем диапазон
    if 1 <= k <= 365:
        # 1 января - четверг (4-й день недели)
        day = (4 + k - 1) % 7
        # Возвращаем номер дня недели
        return day
    else:
        return "Ошибка: Введите число от 1 до 365."

# Пример использования
k = int(input("Введите номер дня года (от 1 до 365): "))
result = day_of_week(k)
if isinstance(result, int):
    print(f"Номер дня недели: {result}")
else:
    print(result)
