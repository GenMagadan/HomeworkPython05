# Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии. Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = float(input("Введите число A: "))
b = int(input("Введите степень B: "))


def func(number, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (number * func(number, - power - 1))
    return number * func(number, power - 1)


print(f'{int(a)} ^ {b} = {func(a, b)}')
