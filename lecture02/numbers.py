import math

number = int(input("Введите число от 0 до 99: "))

numbers0 = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
numbers10 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",\
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
numbers20 =["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]


if number <= 9:
    print(numbers0[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(numbers10[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    duos = ones - 2
    tens = number % 10
    if tens == 0:
        print(numbers20[duos].capitalize())
    elif tens != 0:
        print(numbers20[duos].capitalize() + " " + numbers0[tens])