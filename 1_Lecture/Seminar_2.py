"""
# Задача_9: 

# Решение в группах
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while

# Input: 5
# Output: 120

# Факториал умножается на 1, поэтому нельзя умножать на 0

# РЕШЕНИЕ_ЗАДАЧИ_9

#Решение_1

n = int(input('Введите число :'))
i = 1
f = 1
while i <= n:
    f = f * i
    i += 1
print(f)

#Решение_2

num = int(imput())
k = 1
temp = 1
while temp <= num:
    k *= temp
    temp += 1
print(k)

"""

"""
# Задача 10:

# На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите 
# минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# РЕШЕНИЕ_ЗАДАЧИ_10

#Решение_1

c = 'ООРРРОООРОРОРРРРОРОРРРРРРР'
p = 'Р'

head = 0
tail = 0

for i in c:
    if i == p:
        head += 1
    else:
        tail += 1
if head < tail:
    print(f'Минимальное кол-во монет, котрые необходимо перевернуть : {head}')
else:
    print(f'Минимальное кол-во монет, котрые необходимо перевернуть : {tail}')


#Решение_2   
 
# n = int(input())
# count_zero = 0
# count_one = 0

# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#     if count_one > count_zero:
#         print(count_zero)
# else:
#     print(count_one)    
    
"""

"""
# Задача 11:

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# РЕШЕНИЕ_ЗАДАЧИ_11

#Решение_1
# a = int(input())

# fib1 = 0
# fib2 = 1
# n = 2

# while fib2 < a:
#     fib1, fib2 = fib2, fib1 + fib2
#     n += 1

# if fib2 == a:
#     print(n)
# else:
#     print(-1)

#Решение_2 - не завершено
# n = int(input('Введите число :'))
# f = 1
# i = 1
# while f <= n:
#     if f == n:
#         print(i)
#     f = f + i
#     i += 1
# print(i+2)

"""

"""
# Задача 12: 

# Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# РЕШЕНИЕ_ЗАДАЧИ_12

#Решение_1 - через дискриминант

# import math

# S = 10
# P = 24

# D = S ** 2 - 4 * P

# if D < 0:
#     print('Петя посчитал некорректно : ')

# Y1 = int((S + math.sqrt(D)) / 2)
# Y2 = int((S - math.sqrt(D)) / 2)

# X1 = S - Y1
# X2 = S - Y2

# if X1 == Y2:
#     print ((X1, X2))
# else:
#     print((X1,Y1),(X2, Y2))

#Решение_2 - через бинарный поиск и цикл

numberS = int(input("Сумма загаданных чисел равна"))
numberP = int(input("Произведение загаданных чисел равна"))

def binFind(numS, numP):
    left = 1
    right = numS//2 + 1
    while left <= right:
        middle = (left + right) // 2
        if numP/middle == numS - middle:
            return middle
        elif middle * (numS - middle) < numP:
            left = middle + 1
        else: right = middle - 1
    else: return None
x = binFind(numberS, numberP)

if x != None:
    y = numberS - x
    print(f"Петя загадал числа {x} и {y}")
else: print("НЕТ РЕШЕНИЙ")

#Решение_3

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

"""


"""

# Задача_13: 

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# РЕШЕНИЕ_ЗАДАЧИ_13

#Решение_1

# n = int(input('Введите число дней :'))
# i = 1
# days = 0
# while i < n:
#     tempr = int(input('Введите среднесуточную температуру'))
#     if t > 0:

import random
days = int(input('Кол-во дней:'))
if days >= 1 and days <= 100:
    #temperature = [int(input(f"Температура - день {i + 1}: ")) for i in range(days)] #Ручной ввод показаний
    temperature = []
    maxHotCount = 0
    tempCount = 0
    for i in range(days):
        temperature.append(random.radint(-50,50)) #Выключить при активации ручного ввода показаний
        if temperature[i] > 0:
            tempCount += 1
            if tempCount > maxHotCount: # текущий список обнуляется если отрицательная температура
                maxHotCount = tempCount
        else: tempCount = 0
    print(f"{temperature} -> {maxHotCount}")
else: print("Некорректный ввод (1 ≤ N ≤ 100)")

"""

"""
# Задача 14: 

# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8


# РЕШЕНИЕ_ЗАДАЧИ_14

#Решение_1

import math
num = int(input("Введите число : "))
i = 0
while pow(2,i) <= num:
    print(pow(2,i),end = " ")
    i += 1

#Решение_2 

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

"""

"""

# Задача_15:

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# РЕШЕНИЕ_ЗАДАЧИ_15

#Решение_1

n = int(input())
arb = int(input())
maxarb = arb
minarb = arb
for i in range (n-1):
    arb = int(input())
    if arb > maxarb:
        maxarb = arb
    if arb < minarb:
        minarb = arb
print(minarb, maxarb)


"""

"""

# Задача_*
# Дана строка текста, сосотоящая из букв русского алфавита
# "O" и "Р". Буква "O"  соответствует выпаданию орла, а буква
# "Р" - Решки. Напишите программу, которая подсчитывает наибольшее 
# колличество подряд выпавших Решек.

# Решение_1

# inp = input()
# строка разбивается на массив с разделител большое О
# split режет массив на элементы, поэлементно, в виде
# списка элементов
# a = inp.split("О")
# Выводится максимальная длина из массива a
# print(len(max(a)))

# Решение_2
# Условие как накопитель - динамическое
# Постоянно увеличивается

# s = input()
# t = 0
# while "Р"*(t+1) in s:
#     t += 1
# if t != 0:
#     print(t)
# else:
#     print(0)

"""
