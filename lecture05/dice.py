import random

def dice_settings():
    while True:
        settings = input("Введите число кубиков и количсетво сторон: ")
        if "d" in settings:
            left, right = settings.split("d")
            if left.isdigit() and right.isdigit():
                return int(left), int(right)
            print("Введённое значение должно быть записано в виде NdM")

dice = dice_settings()
N = dice[0]
M = dice[1]

def probability():

    properties = [[0 for j in range(N * M)]
          for i in range(N + 1)]

    for i in range(M):
        properties[1][i] = 1 / M

    for i in range(2, N + 1):
        for j in range(len(properties[i - 1])):
            for k in range(M):

                if (properties[i - 1][j] != 0 and
                        properties[i - 1][k] != 0):
                    properties[i][j + k] += (properties[i - 1][j] * properties[1][k])

    for i in range(len(properties[N]) - N + 1):
        print("%d %0.3f" % (i + N, properties[N][i]*100),'%')

probability()