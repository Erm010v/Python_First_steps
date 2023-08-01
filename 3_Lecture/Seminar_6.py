"""
# Задача_30:

# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# РЕШЕНИЕ_ЗАДАЧИ_30

# Решение_1

a1 = 7
d = 2
n = 5
for i in range(n):
    print(a1 + i * d, end=' ')
"""
# Решение_2 - Для списка с целыми значениями (неполное_доработать)
# a, d, n = map(int, input('a1 d n » ').split())
# p = [a + i * d for i in range(n)]

"""
# Решение_3 - Для списка с необязательно целыми значениями членов прогрессии (неполное_доработать):
a, d, n = map(float, input('a1 d n » ').split())
p = [a + i * d for i in range(int(n))]
"""

"""
# Задача_32:

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше
# заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# РЕШЕНИЕ_ЗАДАЧИ_32

# Решение_1

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_2 = []
# max = 10
# min = 6
# for i in range(len(lst_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
# или
# for i in range(len(list_1)):
#     if min <= list_1[i] <= max:
#         print(i, end=' ')
"""

"""
# Задача_39:

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# РЕШЕНИЕ_ЗАДАЧИ_39

# Решение_1

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1


# Вывод:
# 3 3 2 12

# РЕШЕНИЕ_ЗАДАЧИ_39

# Решение_1

# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# print(list_1)

# m = int(input())
# list_2 = list()
# for i in range(m):
#     x = int(input())
#     list_2.append(x)

# print(list_2)

# for number in list_2:
#     a = list_1.count(number)
#     if a > 0:
#         for i in range(0, a):
#             list_1.remove(number)
# print(list_1)
"""

"""
# Задача_41:

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:
# 5
# 1 2 3 4 5

# Вывод:
# 0

# Ввод:
# 5
# 1 5 1 5 1

# Вывод:
# 2

# РЕШЕНИЕ_ЗАДАЧИ_41

# Решение_1

# import random
# list_1 = [random.randint(1, 9) for i in range(8)]
# print(list_1)
# count = 0
# for i in range(1, len(list_1)-1):
#     if list_1[i+1] < list_1[i] > list_1[i-1]:
#         count += 1
# print(count)
"""

"""
# Задача_43:

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:
# 1 2 3 2 3

# Вывод:
# 2

# # РЕШЕНИЕ_ЗАДАЧИ_43

# # Решение_1


# a = input().split()
# print(sum(a.count(x) - 1 for x in a) // 2)
"""

"""
# Задача_45:

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:
# 300

# Вывод:
# 220 284

# # РЕШЕНИЕ_ЗАДАЧИ_45

# # Решение_1 - считать и проверять

def summa(a):
    result = 0
    for i in range(1, a):
        if a % i == 0:
            result += i
    return result


k = 300

list_1 = []
for i in range(1, k + 1):
    if i not in list_1:
        j = summa(i)
        if i != j and summa(j) == i:
            list_1.append(j)
            print(i, j)

# # Решение_2 - создать список из кортежей




"""
