
# Задача 34:

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они
# разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам

# РЕШЕНИЕ_ЗАДАЧИ_34

# Решение_1
"""
def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
"""

# Решение_2
"""
inp = "пара-ра-рам рам-пам-папам па-ра-па-дам"
answerRight = "Парам пам-пам"
answerWrong = "Пам парам"
vowels = ['у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']

print(answerRight
      # x for x in l.lower() if x in vowels - новый список только из гласных элементов
      # lambda l: len([x for x in l.lower() if x in vowels] - лябда функции вычисляет длину
      # делается множество set(map(lambda l.....
      # проверка длины, если равно 1, тогда списки с одинаковым кол-вом гласных
      if len(set(map(lambda l: len([x for x in l.lower() if x in vowels]), inp.split()))) == 1
      else answerWrong
      )
"""
# Решение_3

# в списке countVowels счетчик count считает кол-во countVowels с индексом 0
# далее сравнивает с длиной списка
# countVowels.count(countVowels[0]) == len(countVowels):
# если все равны, тогда count равен длине списка


# Задача_36:

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)

# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# РЕШЕНИЕ_ЗАДАЧИ_36


# Решение_1
"""
def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)]
         for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)
"""

# Решение_2

"""
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=" ")
        print()


print_operation_table(lambda x, y: x * y)
"""

# Задача_47:

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

# РЕШЕНИЕ_ЗАДАЧИ_47

# Решение_1
"""
def transformation(x): return x


values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
"""


# Задача_49:

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна


# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# РЕШЕНИЕ_ЗАДАЧИ_49

# # Решение_1
"""
# Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def is_circle(tup):
    if tup[0] == tup[1]:
        return None
    else:
        return tup


def find_square(tup):
    x = 3.14 * tup[0] * tup[1]
    return x


def find_farthest_orbit(list_of_orbits):
    # true_orbits = list(map(is_circle, list_of_orbits))
    list_of_squares = list(map(find_square, list_of_orbits))
    return max(list_of_squares)


print(find_farthest_orbit(orbits))

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]))
"""


# Задача_51:

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# Вывод:
# same

# РЕШЕНИЕ_ЗАДАЧИ_51:

# Решение_1
"""
def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False


def char(x):
    return x % 2 == 0


values = [2, 4, 5]
print(same_by(char, values))
"""
