# def f(x):
#     return x*x
# print(f(5)) - выводится 25
# a = f
# print(a(5)) - выводится 25

# def calc1(a, b):
#     return a + b

"""
def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a + b, 5, 45)
"""

"""
# def calc1(a, b):
#     return a + b

# def calc1(a, b): return a + b

math(calc2, 5, 45)
"""

# Задача_1:

#  В списке хранятся числа. Нужно выбрать только чётные
# числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

"""
# Решение_1:

data = [1, 2, 3, 5, 8, 15, 23, 38]  # есть список из условия
result = list()  # Создание списка result, кот-й выводит результат

for i in data:  # прохождение по всем элементам из списка дата
    # каждый раз проверяем если знаячения в списке
    # делятся на 2 без остатка, тоесть число четное
    if i % 2 == 0:
        # тогда в список result добавляем новое значение
        result.append((i, i ** 2))  # передаем в виде кортежа - 2 скобки
print(result)
"""
# Решение_2 - lambda:

"""
def select(f, col):  # передаем саму функцию f и значение col
    # она возвращает список, в котором применяется
    # к каждому элементу f от x
    # но мы проходимся по всем элементам for i in col
    return [f(x) for x in col]

# напишем 2-ю функцию, где мы также передаем 2 значения
# f и col


def where(f, col):
    # она возвращает список, в котором применяется
    # к каждому элементу, но возвращает x с условием
    # если выполнилось f от x
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
# создаем список res - через select
# приводим к целочисленному типу - int
res = select(int, data)
print(res)
# обращаемся к списоку res и делаем выборку ч/з where
# lambda принимает значение x либо True либо False
# остаток от деления - целое число
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x ** 2), res)  # возвращается кортеж из элементов x
print(res)

"""
# Функция map

# Функция map() применяет указанную функцию к каждому
# элементу итерируемого объекта и возвращает итератор
# с новыми объектами. Принимает на вход 2 аргумента:
# 1-й сама функция, которую передаем
# 2-й объект

"""
# список лист 1 через генератор списка
list_1 = [x for x in range(1, 20)]
print(list_1)
# результат:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
# результат:
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
"""

"""
# Задача_2:

# C клавиатуры вводится некий набор чисел, в качестве
# разделителя используется пробел. Этот набор чисел будет
# считан в качестве строки. Как превратить list строк в list чисел?

# .split (' ,') # разделитель строки через ,
# я строка.split() - убирает все пробелы и создаем
# список из значений строки, пример:

# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '', '15', '23', '38']

data = '1 2 3 5 8 15 23 38'
# print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)
"""

"""
# Функция filter

# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами,
# для которых функция вернула True.

# filter() позволит избавиться от функции where

data = [15, 65, 9, 36, 175]
# выводятся только те элементы, которые оканчиваются на 5
res = list(filter(lambda x: x % 10 == 5, data))
print(res)


data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
"""

"""
# Функция zip

# Функция zip() применяется к набору итерируемых объектов и
# возвращает итератор с кортежами из элементов входных данных

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) 
# [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

Функция zip () пробегает по минимальному входящему набору:
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
"""

"""
# Функция enumerate

# Функция enumerate() позволяет пронумеровать набор данных.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)

# [(0, 'user1'), (1, 'user2'), (2, 'user3))]
"""

"""
# Файлы


# 1. Режим a
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# ● data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.

# Ещё один способ записи данных в файл:

with open('file.txt', 'w') as data:
data.write('line 1\n')
data.write('line 2\n')

# 2. Режим r
# ● Чтение данных из файла:

path = 'file.txt'
data = open(path, 'r')
for line in data:
print(line)
data.close()

# 3. Режим w

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()

"""
"""
# Модуль os

# Модуль os предоставляет множество функций для работы с операционной
# системой, причем их поведение, как правило, не зависит от ОС, 
# поэтому программы остаются переносимыми.
# Для того, чтобы начать работать с данным модулем необходимо его 
# импортировать в свою программу:

import os
# Познакомимся с базовыми функциями данного модуля:
# ● os.chdir(path) - смена текущей директории.
import os
os.chdir('C:/Users/79190/PycharmProjects/GB')
# ● os.getcwd() - текущая рабочая директория
import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject

# ● os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как:
# ○ os.path.basename(path) - базовое имя пути
import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
'main.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
import os
print(os.path.abspath('main.py'))
# 'C:/Users/79190/PycharmProjects/webproject/main.py'

"""

# Модуль shutil

# # Модуль shutil содержит набор функций высокого уровня для обработки 
# # файлов, групп файлов, и папок. В частности, доступные здесь функции
# # позволяют копировать, перемещать и удалять файлы и папки. Часто 
# # используется вместе с модулем os.
# # Для того, чтобы начать работать с данным модулем необходимо его
# # импортировать в свою программу:

# import shutil
# # Познакомимся с базовыми функциями данного модуля:
# # ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# # файл dst.
# # ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# # ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# # должен указывать на директорию, а не на символическую ссылку.