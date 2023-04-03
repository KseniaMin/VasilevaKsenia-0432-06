string = input("Введи что-нибудь - ")
for i in range(len(string)):
    if i == 2:
        continue
    elif string[i] == "c":
         print("Найден символ 'c'!")
print("Последний символ строки:", string[i])
print("Длина строки:", len(string))
print("Строка без последнего символа:", string[:-1])
