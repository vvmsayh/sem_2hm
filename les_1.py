# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
# from unittest import result


# number = float(input("введите вещественное число: "))


# def remove_dot_from_float(n):
#     while n % 10 != 0:
#         n = round(n * 10, 7)
#     return int(n // 10)


# num_int = remove_dot_from_float(number)



# result=0
# while number>0:
#     result += number % 10
#     number //= 10
# print(round(result))

n = input("Введите число = ").replace('.', '')
while not n.isdigit():
    n = input("Введите число = ").replace('.', '')
    
my_sum = 0
# for i in s:
#     my_sum += int(i)
s = list(n3)
print(map(int,s))
my_sum = sum(list(map(int,s)))
print(my_sum)


# num = input('Введите вещественное число: ')
# while not num.lstrip('-').replace('.', '',1).isdigit(): num = input('Введите вещественное число: ')  
# print(sum(list(map(int, num.lstrip('-').replace('.', '', 1)))))

