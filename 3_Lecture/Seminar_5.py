
# Задача_26:

# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# РЕШЕНИЕ_ЗАДАЧИ_26

#Решение_1




"""
# Задача_28:

# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1
# и -1. Также нельзя использовать циклы.

# 2 2
# 4

# РЕШЕНИЕ_ЗАДАЧИ_28

#Решение_1

"""



# Задача_31

# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# РЕШЕНИЕ_ЗАДАЧИ_31

#Решение_1




"""
# Задача_33:

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# РЕШЕНИЕ_ЗАДАЧИ_33

#Решение_1

# import random

# score_list = [1, 3, 3, 3, 4]
# print(score_list)

# new_score_list = []

# for i in score_list:
#     if i == max(new_score_list):
#         new_score_list.append(min(score_list))
#     else:
#         new_score_list.append(i)
# print(new_score_list)

#Решение_2

# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# max_number = max(list_1)
# min_number = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_number:
#         list_1[i] = min_number
# print(list_1)
"""



# Задача_35:

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# РЕШЕНИЕ_ЗАДАЧИ_35

#Решение_1




# Задача_37:

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# РЕШЕНИЕ_ЗАДАЧИ_37

#Решение_1


# Задача_*:

# Найти факториал числа через рекурсию:

num = 4

def fact(num):
    if num==1:
        return num
    return num*fact(num-1)

print(fact(num))
