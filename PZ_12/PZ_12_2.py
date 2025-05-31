# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def up(d):
    for i in d:
        yield (lambda c: c.upper())(i)
fraz = input("Введите фразу:")
for b in up(fraz):
    print(b, end="")