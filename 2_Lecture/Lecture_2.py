# Лекция_2

# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]

# выводить список со скобками
#print(list_1)

# убрать все скобки из выводимых данных
#print(*list_1)

# вывести цифры сверху вниз
#for i in list_1:
#    print(i)

# вывод кол-ва всех элементов
# print(len(list_1))

# вывод первого элемента
# print((list_1[0]))

# вывод начиная с последнего элемента
# print((list_1[-1]))

# функция append позволяет добавить элекмент в конец списка

# list_1 = [1,5]
# print(list_1)
# list_1.append(88)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# Метод pop удаляет последний элемент из списка:
# pop не только удаляет последний элемент, но и добавляет 0

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0

# Вывести весь список
# print(list_1[:])

# Создание КОРТЕЖА - неизменяемого списка

# t = ()

# print(type(t))

# t = (1, 5, 3, )
# print(type(t))

# # Список, но пока еще не КОРТЕЖ
# v = [1, 8, 9]
# print(v)
# print(type(v))

# # уже КОРТЕЖ
# v = tuple(v)
# print(v)
# print(type(v))

                      # # КОРТЕЖ разделим на 3 переменных

# # a, b = 1, 2
# # a = b = 1

# a,b,c = v

# print(a,b,c)

# t = (1, 2, 3, 5)

# for i in range(len(t)):
#     print(t[i])

                             # Работа со СЛОВАРЕМ

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d ['q'])

#Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
#В списках в качестве ключа используется индекс элемента.
#В словаре для определения элемента используется значение ключа (строка, число).
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отл
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# for item in dictionary: 
    # for (k,v) in dictionary.items():
    # print('{}:{}'.format(item, dictionary[item]))
    # print(item)



# dictionary[895] = 98998
# print(dictionary)


                               # # МНОЖЕСТВА

# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok

# Удалить все записи из множества
# print(color) # set()

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

#Неизменяемое или замороженное множество(frozenset)
#  — множество, с которым не будут
# работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# У каждого языка программирования есть свои особенности и преимущества. Одна из
# культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке.

# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]

# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# ЗАДАЧИ: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.

# Решение:

# 1. Создать список чисел от 1 до 100

# list_1 = []
# for i in range(1, 101)
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)

# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. 
# Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# Самые распространенные ошибки:

# ОШИБКА_1 
# Отсутствие :
# SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!! # ПРОПУЩЕНО :
#  print(number_first)

# ОШИБКА_2
# Отсутствие отступов
# IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!

# ОШИБКА_3
# Нельзя складывать строки и числа
# TypeError(Типовая ошибка)
# text = 'Python'
# number = 5 # '5' рещение
# print(text + number)

# ОШИБКА_4
# Делить на 0 нельзя
# ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)

# ОШИБКА_5
# Такого ключа не существует
# KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])

# ОШИБКА_6
# Переменной names не существует
# NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)

# ОШИБКА_7
# Нельзя символы перевести в целые значения
# ValueError(Ошибка значения)
# text = 'Python' # '555' - просто написать число
# print(int(text))
