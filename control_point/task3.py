from collections import Counter

string = input("Введите строку: ")

res = Counter(string)

print ("Число элементов :\n " + str(res))