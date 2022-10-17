# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

#______________________________________________________

# random import randint

# N = int(input("Введите длину последовательности: "))
# list_random = []
# for i in range (0, N):
#     list_random.append(str(randint(1,9)))
# list_random = ''.join(list_random)
# print(list_random)

# list_digitcount = {}
# for j in list_random:
#     if list_digitcount.get(j):
#         list_digitcount[j] = list_digitcount.get(j) + 1
#     else:
#         list_digitcount[j] = 1

# list_uniques = []
# for k in list_digitcount.items():
#     if k[1] == 1:
#         list_uniques += str(k[0])

# if list_uniques:
#     print(f"Неповторяющиеся цифры списка {list_uniques}")
# else:
#     print("Неповторяющиеся цифры отсутствуют") 

from random import randint

#_________________________________________________________________

list_random = ''.join([str(randint(1,9)) for i in range (int(input("Введите длину последовательности: ")))])
print(list_random)
dict_digitcount = {i : list_random.count(i) for i in list_random}
list_uniques = list(filter(lambda i: dict_digitcount[i] == 1, dict_digitcount.keys()))
print(f"Неповторяющиеся цифры списка {list_uniques}" if list_uniques else "Неповторяющиеся цифры отсутствуют")
