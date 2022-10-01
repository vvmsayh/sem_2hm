#перемешивание списка
import random
list = [11, 2, 23, 34, 55, 16]
for i in range(len(list)):
    a =  random.randint(0,len(list) -1)
    if i != a:
        list[i],list[a] = list[a],list[i]
        print(list[i], list[a])
print(list)
