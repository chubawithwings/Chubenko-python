import tkinter as tk

def find_unique():
    try:
        values = entry.get().split()
        if len(values) != 4:
            result_label.config(text="Введите ровно 4 числа")
            return
        a, b, c, d = map(int, values)

        if a == b == c == d:
            result = "Все числа одинаковые"
        elif a == b == d:
            result = "Порядковый номер отличного числа: 3"
        elif a == c == d:
            result = "Порядковый номер отличного числа: 2"
        elif b == c == d:
            result = "Порядковый номер отличного числа: 1"
        elif a == b == c:
            result = "Порядковый номер отличного числа: 4"
        else:
            result = "Ошибка: нет одного уникального числа"
    except ValueError:
        result = "Ошибка: введите целые числа"

    result_label.config(text=result)

root = tk.Tk()
root.title("Поиск уникального числа")

tk.Label(root, text="Введите четыре целых числа через пробел:", font="Arial 14").pack(pady=10)
entry = tk.Entry(root, font="Arial 14")
entry.pack(pady=5)

tk.Button(root, text="Проверить", font="Arial 14", command=find_unique).pack(pady=5)
result_label = tk.Label(root, text="", font="Arial 14", fg="blue")
result_label.pack(pady=10)

root.mainloop()