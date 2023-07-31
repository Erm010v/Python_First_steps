
# Задача_26:

# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# РЕШЕНИЕ_ЗАДАЧИ_26

# Решение_1

# def recAB(a, b):
#     if b == 0:
#         return 1
#     return a * recAB(a, b - 1)


# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(recAB(a, b))


# Задача_28:

# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1
# и -1. Также нельзя использовать циклы.

# 2 2
# 4

# РЕШЕНИЕ_ЗАДАЧИ_28

# Решение_1

# a = int(input("Введите первое неотрицательное число: "))
# b = int(input("Введите второе неотрицательное число: "))
# if a > b:
#     a, b = b, a


# def recursive_sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return recursive_sum(a - 1, b + 1)


# print(recursive_sum(a, b))


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
# Output: 13

# РЕШЕНИЕ_ЗАДАЧИ_31

# Решение_1

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(7))
"""

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

"""
# Задача_35:

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# РЕШЕНИЕ_ЗАДАЧИ_35

# Решение_1

def isPrime(n, delim=2):
    if n < 2:
        return False
    if n == 2 or delim * delim > n:
        return True
    if n % delim == 0:
        return False
    return isPrime(n, delim + 1)
# if delim * delim > n - точно будет простое число, дальнейщая проверка не требуется


print(isPrime(101))
"""

"""
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

# Решение_1

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1) + f' {k}'


# n = int(input())
# print(f(n))

# Решение_2

# def polindrom(word):
#     if len(word) < 2:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     return polindrom(word[1:-1])


# print(polindrom("арозаупаланалапуазора"))
"""

"""
# Задача_*:

# Найти факториал числа через рекурсию:

# Решение_*
num = 3


def fact(num):
    if num == 0:
        return num+1
    return num*fact(num-1)


print(fact(num))
"""
