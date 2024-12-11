#Дни недели пронумерованы следующим образом: 0 — воскресенье, 1 понедельник, 2 — вторник, ...,
#6— суббота. Дано целое число К, лежащее в диапазоне 1-365.
#Определить номер дня недели для К-го дня года, если известно, что в этом году 1 января было четвергом
try:
    K = int(input("Введите номер дня года (1-365): "))
    if K < 1 or K > 365:
        print("Ошибка: номер дня года должен быть в диапазоне от 1 до 365.")
    else:
        day_of_week = (4 + K - 1) % 7
        print(f"Номер дня недели для {K}-го дня года: {day_of_week}")
except ValueError:
    print("Ошибка введите число (1-365)")