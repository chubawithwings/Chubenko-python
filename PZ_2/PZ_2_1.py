try:
    K = int(input("Введите номер дня года (1-365): "))
    if K < 1 or K > 365:
        print("Ошибка: номер дня года должен быть в диапазоне от 1 до 365.")
    else:
        day_of_week = (4 + K - 1) % 7
        print(f"Номер дня недели для {K}-го дня года: {day_of_week}")
except ValueError:
    print("Ошибка: введите целое число.")