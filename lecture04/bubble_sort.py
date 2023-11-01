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

for i in range(n-1):
    for j in range(0, n-i-1):
        if randoms[j] > randoms[j + 1]:
            randoms[j], randoms[j + 1] = randoms[j + 1], randoms[j]

print ("Отсортированный список: ")

print (randoms, end = " ")