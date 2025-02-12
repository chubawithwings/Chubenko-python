#Дан символ C и строки S, S0. После каждого вхождения символа C в строку S вставить строку S0

def insert_symbol (C, S, S0):
    return S.replace(C, C + S0)
S ="nvdjjdvjvjd"
C = "j"
S0 = "XXXXX"

result = insert_symbol(C, S, S0)
print(result)
