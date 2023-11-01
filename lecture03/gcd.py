flag = 1

while flag:
    a = input('Введите число a: ')
    b = input('Введите число b: ')
    if a.isdigit() and b.isdigit():
        flag = 0
else:
    if a.isdigit() or b.isdigit():
        a = float(a)
        b = float(b)

        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        print(a + b)

flag = 1