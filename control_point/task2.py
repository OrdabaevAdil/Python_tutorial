s = input("Введите два слова: ")
b = s.split()
str1 = b[0]
str2 = b[1]

str1 = str1.lower()
str2 = str2.lower()

a = list(set(str1) & set(str2))
a = sorted(a)
print("Общие буквы: ")
for i in a:
    print(i)