# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
from unittest import result


number = float(input("введите вещественное число: "))


def remove_dot_from_float(n):
    while n % 10 != 0:
        n = round(n * 10, 7)
    return int(n // 10)


num_int = remove_dot_from_float(number)



result=0
while number>0:
    result += number % 10
    number //= 10
print(round(result))

