# приложение сдача в аренду торговых площадей для некоторой организации. бд 
# должна содержать таблицу Торговая точка со след структурой записи: 
# этаж, площадь, наличие кондиционера и стоимость аренды в день


import sqlite3

with sqlite3.connect('arenda.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS torg_t
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor INTEGER NOT NULL,
                pl INTEGER NOT NULL,
                have_cond BOOLEAN NOT NULL,
                cost_day INTEGER NOT NULL);""")

    data = [
        (1, 20, True, 1000),
        (2, 35, False, 1800),
        (3, 25, True, 1600),
        (1, 40, True, 2100),
        (2, 22, False, 1200),
        (3, 30, True, 1700),
        (1, 28, False, 1400),
        (2, 50, True, 2500),
        (3, 18, False, 900),
        (1, 33, True, 2000)
    ]
    cursor.executemany("""INSERT INTO torg_t (floor, pl, have_cond, cost_day) VALUES (?, ?, ?, ?)""", data)
    conn.commit()

    # поиск по этажу
    cursor.execute("SELECT * FROM torg_t WHERE floor = 1")
    print(cursor.fetchall())

    # поиск по наличию кондиционера
    cursor.execute("SELECT * FROM torg_t WHERE have_cond = True")
    print(cursor.fetchall())

    # поиск стоимость в день <= 1500
    cursor.execute("SELECT * FROM torg_t WHERE cost_day <= 1500")
    print(cursor.fetchall())
    
    # удаление по этажу = 3
    cursor.execute("DELETE FROM torg_t WHERE floor = 3")
    print('удалила по этажу')
    conn.commit()

    # удаление площадей меньше 25
    cursor.execute("DELETE FROM torg_t WHERE pl < 25")
    print('удалила по площади')
    conn.commit()

    # удаление без кондиционера
    cursor.execute("DELETE FROM torg_t WHERE have_cond = False")
    print('удалила по наличию кондиционера')
    conn.commit()

    # увеличить стоимость на 10% на 1 этаже
    cursor.execute("UPDATE torg_t SET cost_day = cost_day * 1.1 WHERE floor = 1")
    print('увеличила цену')

    # изменить площадь на 45.0 там, где стоимость > 2000
    cursor.execute("UPDATE torg_t SET pl = 45.0 WHERE cost_day > 2000")
    print('изменила площадь')

    # установить кондиционер = False, если площадь > 40
    cursor.execute("UPDATE torg_t SET have_cond = False WHERE pl > 40")
    print('изменила наличие кондиционера')
    conn.commit()