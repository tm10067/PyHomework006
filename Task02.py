# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#_________________________________________________________________________

# from random import random

# N = int(input("введите длину списка: "))
# list = []
# max_range = 20
# min_range = 1
# for i in range(N):
#     list.append(round(random() * (max_range - min_range) + min_range, 2))
# print(list)
# list_fractions = []
# for j in list:
#     if j != int(j):
#         list_fractions.append(round(j - int(j), 2))
# print(list_fractions)
# print(round(max(list_fractions) - min(list_fractions), 2))

#__________________________________________________________________________

from random import random

max_range = 20
min_range = 1
list = [round(random() * (max_range - min_range) + min_range, 2) for i in range(int(input("введите длину списка: ")))]
print(list)
list_fractions = [round(j - int(j), 2) for j in list if j != int(j)]
print(list_fractions)
print(round(max(list_fractions) - min(list_fractions), 2))
