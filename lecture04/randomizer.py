import random

randoms = []

while True:
    try:
        n = int(input("Введите целое число элементов: "))
        limit = int(input("Введите максимальное число: "))
    except ValueError:
        continue
    else:
        break

for i in range(n):
    randoms.append(random.randint(1, limit))
print(randoms)