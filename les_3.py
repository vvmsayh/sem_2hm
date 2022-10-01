# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}---неправильный
# from cgi import print_environ
# import fractions
# from tkinter import N
# number = float(input("Введите число для последовательности: "))
# step=float
# list=[1,step]
# for i in range(1,int(number)):
#     step=round((1+1/number)**number,1)
#     number+=1
#     list=[1,step]
#     print(list)
n = int(input('Введите число: '))
my_list = [[n, round(((1+1/n)**n),2)] for n in range(1,n+1)]
print('Последовательность чисел: ', dict(my_list))
print('Сумма чисел последовательности: ', sum(dict(my_list)))
