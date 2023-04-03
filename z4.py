import math
import random

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def arccos(n):
    return math.acos(n)

operation = input("Введите символ операции (+, -, /, *, ^, mod, rand, !, acos): ")

if operation == "+":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    result = n1 + n2
    print("Результат: ", result)
elif operation == "-":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    result = n1 - n2
    print("Результат: ", result)
elif operation == "/":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    if n2 == 0:
        print('Делить на ноль нельзя')
    result = n1 / n2
    print("Результат: ", result)
elif operation == "*":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    result = n1 * n2
    print("Результат: ", result)
elif operation == "^":
    n1 = float(input("Введите число: "))
    stepen = float(input("Введите степень: "))
    result = n1 ** stepen
    print("Результат: ", result)
elif operation == "mod":
    n1 = float(input("Введите число: "))
    mod = float(input("Введите делитель: "))
    result = n1 % mod
    print("Результат: ", result)
elif operation == "rand":
    low = float(input("Введите нижнюю границу диапазона: "))
    high = float(input("Введите верхнюю границу диапазона: "))
    result = random.uniform(low, high)
    print("Результат: ", result)
elif operation == "!":
    n = int(input("Введите число для вычисления факториала: "))
    result = factorial(n)
    print("Результат: ", result)
elif operation == "acos":
    n = float(input("Введите число для вычисления арккосинуса: "))
    result = arccos(n)
    print("Результат: ", result)
else:
    print("Неверный символ операции")