# 2. Напишите программу, которая найдёт произведение пар чисел списка 
# (Cписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

#_____________________________________________________

# from random import randint

# N = int(input("введите длину списка: "))
# list = []
# for i in range(N):
#     list.append(randint(1,10))
# print(list)
# list_mult = []
# for j in range(N // 2):
#     list_mult.append(list[j] * list[N - j - 1])
# print(list_mult)

#_____________________________________________________


from random import randint

N = int(input("введите длину списка: "))
list = [randint(1,10) for i in range(N)]
print(list)
list_mult = [list[j] * list[N - j - 1] for j in range (N // 2)]
print(list_mult)
