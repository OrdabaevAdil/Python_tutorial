N = 1
flag = 1
b = []
while flag:
    N = input('Введите число: ')
    if N.isdigit():
        flag = 0
    else:
        print('Не верный ввод')
else:
    if N.isdigit():
        N = int(N)
        for i in range(2,N + 1):
            b.append(i)
        p = [True for i in range(N + 1)]
        p[0] = p[1] = False
        i = 2
        while i * i <= N:
            if p[i]:
                j = i * i
                while j <= N:
                    p[j] = False
                    j += i
            i += 1

        for j in range(len(p)):
            if p[j]:
                print(b[j - 2])

    flag = 1



