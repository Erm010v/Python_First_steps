"""
# Задача_22:

# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого 
# множества. m - кол-во элементов второго множества. Затем 
# пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# РЕШЕНИЕ_ЗАДАЧИ_22

#Решение_1

# n = int(input('Введите кол-во элементов в первом наборе чисел: '))
# a = list()

# for i in range(n):
#     a.append(int(input(f'Введите {i+1} элемент: ')))
# print(f'Первый набор: {a}')
# a1 = set(a)
# m = int(input('Введите кол-во элементов во втором наборе чисел: '))
# b = list()
# for i in range(m):
#     b.append(int(input(f'Введите {i+1} элемент: ')))
# print(f'Второй набор: {a}')
# b1 = set(b)
# c = sorted(a1.intersection(b1))
# print(f'Повторяющиеся элементы: {c}')

#Решение_2

# import random
# n = int(input('Введите кол-во элементов в первом наборе чисел: '))
# n = int(input('Введите кол-во элементов в первом наборе чисел: '))

# nums1 = [random.randint(0,10) for i in range(n)]
# nums2 = [random.randint(0,10) for i in range(m)]

# print(*nums1)
# print(*nums2)

# new_nums = []
# for i in nums1:
#     if i in nums2 and not i in new_nums:
#         new_nums.append(i)

# print(*sorted(new_nums))
"""

"""
# Задача_24: 

# В фермерском хозяйстве в Карелии выращивают чернику.
#  Она растет на круглой грядке, причем кусты высажены только по 
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной
# урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора
# черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого 
# куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной
# во входном файле грядки.

# РЕШЕНИЕ_ЗАДАЧИ_24

#Решение_1 - движение списка 

# import random
# n = int(input("Введите кол-во кустов : "))

# garden = [random.randint(1, 6) for i in range(n)]
# print(*garden)

# max_bushes = garden[0] + garden[1] + garden[2]
# indicator = ["|"] * 3 + [" "] * (len(garden) - 3)
# for i in range (len(garden)):
#     following_bushes = garden[1] + garden[2] + garden[3]
#     if following_bushes > max_bushes:
#         max_bushes = following_bushes
#         indicator = ["|"] * 3 + [" "] * (len(garden) - 3)
#     else:
#         temp = indicator.pop(0)
#         indicator.append(temp)
#     temp = garden.pop(0)
#     garden.append(temp)

# print(*indicator)
# print(f" Максимальное число ягод за один раз = {max_bushes} ")

#Решение_2

# import random
# n = int(input("Введите кол-во кустов : "))
# kust = list(random.randint(1,9) for i in range(n))
# print()
# print('На кустах следующее кол-во ягод: ')
# print(kust)
# print()
# maks = 1
# for i in range (-1,len(kust)-1):
#     temp = kust[i-1] + kust[i] + kust[i+1]

# print(kust[i-1], end = ' ')
# print(kust[i], end = ' ')
# print(kust[i+1], end = ' ')
# print(temp)
# print()
# if temp > maks:
#         maks = temp
# print(f'Максимальное кол-во ягод: {maks}')
"""

"""
# Задача_25:

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# РЕШЕНИЕ_ЗАДАЧИ_25

#Решение_1

string = "a a a b c a a d c d d"
text = list(string.split())
letter = {}
result = ''
for i in text:
    if i not in letter:
        letter[i] = 1
        result += f'{i}'
    else:
        result += f'{i}_{letter[i]}'
        letter[i] +=  1
print(result)


# Решение_2 - get - позволяет обращаться к ключу словаря, если нет ключа, тогда выдается строка

string = "a a a b c a a d c d d"
text = list(string.split())
letter = {}
for i in text:
        if i in letter:
            print(f'{i}_{letter[i]}', end = ' ') # end = ' ') - чтобы не было вертикально
        else:
            print(i, end = ' ')         # end = ' ') - чтобы не было вертикально
        letter[i] = letter.get(i,0) + 1 # накопитель (+1), но ключа еще не было
"""


"""
# Задача_27:

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# РЕШЕНИЕ_ЗАДАЧИ_27

#Решение_1

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# uniq = set((text.upper().split())) # множество режется
# print(len(uniq))

#Решение_2

txt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
ltr = {}

for i in txt.lower().split():
    count = ltr.get(i,0)
    if count == 0:
        ltr[i] = 1
    else:
        ltr[i] = count + 1
print(len(ltr))

"""




"""
# Задача_29:
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#   n = int(input())
#   if max_number > n:
#       max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n) 


# РЕШЕНИЕ_ЗАДАЧИ_29

#Решение_1

"""



"""
# Задача_*:

# Формат ввода данных
# Программа должна вывести результат жеребьёвки - Тимур или Руслан, или они сыграли в ничью.
# Примечание. Правила игры стандартные: ножницы режут бумагу.
# Бумага заворачивает камень. Камень давит ящерицу, ящерица травит
# Спока, в то время как Спок ломает ножницы, которые отрезают голову
# ящерице, которая ест бумагу, на которой улики против Спока.
# Спок испаряет камень, а камень затупляет ножницы.

# Решение_Задачи*:

a = input()
b = input()
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур',
     'камень-бумага': 'Руслан', 'камень-ящерица': 'Тимур',
     'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
     'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
     'ножницы-ящерица': 'Тимур', 'ножницы-Спок': 'Руслан',
     'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
     'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан',
     'бумага-Спок': 'Руслан', 'ящерица-ящерица': 'ничья',
     'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
     'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан',
     'Спок-Спок': 'ничья', 'Спок-ножницы': 'Тимур',
     'Спок-бумага': 'Руслан', 'Спок-камень': 'Тимур',
     'Спок-ящерица': 'Руслан'}

a = "камень"
b = "ящерица"

key = f'{a}-{b}'
print(m[key])

"""

# Задача_ХОЛОДИЛЬНИКИ:

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть
# умных холодильников. Теперь он использует их в качестве серверов
# "Пегого дудочника". Помогите владельцу фирмы отыскать все
# зараженные холодильники. Для каждого холодильника существует строка
# с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести
# номер холодильника, нумерация начинается с единицы.

# Формат входных данных

# В первой строке подаётся число n. n – количество холодильников.
# В последующих n строках вводятся строки, содержащие латинские строчные буквы и
# цифры, в каждой строке от 5 до 100 символов.

# Формат выходных данных

# Программа должна вывести номера зараженных холодильников
# через пробел. Если таких холодильников нет, ничего выводить
# не нужно.

# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1:
# 1 2 3

# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton

# Sample Output 2:
# 1 2 7 8

#string = {"1": "222anton456","2": "a1n1t1o1n1","3": "0000a0000n00t00000o000000n","4": "gylfole","5": "richard","6": "ant0n"}

#string = {"1": "osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen","2": "anton","3": "aoooooooooontooooo","4": "elelelelelelelelelel","5": "ntoneeee","6": "tonee","7": "253235235a5323352n25235352t253523523235oo235523523523n","8": "antoooooooooooooooooooooooooooooooooooooooooooooooooooon","9": "unton"}

# Решение_задачи_ХОЛОДИЛЬНИКИ_1:

# def Check_Virus(string, virus):
#     for i in virus:
#         if i not in string:
#             return("OK")
#         else:
#             string = string[string.index(i):]
#         return("Virus")
# for i in string:
#     print(f'{i} - {Check_Virus(string[i], "anton")}')



# inp = 'elelelelelelelelelel'
# etalon = "anton"

# Решение_задачи_ХОЛОДИЛЬНИКИ_2:

# istrue = True
# startindex = 0
# for i in etalon:
#     try:
#         startindex = inp.Index(i,startindex)
#     except:
#         istrue = False
#         break
# print(istrue)

# Решение_задачи_ХОЛОДИЛЬНИКИ_3:

# i = 0
# istrue = False
# while len(inp) > 0: # перебор всех букв и обрезка
#     if inp.startswith(etalon[i]):
#         i += 1
#         if i == len(etalon):
#             istrue = True
#             break
#     inp = inp[1:]
# print(istrue)

# Решение_задачи_ХОЛОДИЛЬНИКИ_4:

# result = []
# n = int(input('Введите кол-во холодильников: '))
# for i in range(n):
#     a,n,t,o,n = 0,0,0,0,0
#     string = str(input(f'Введите строку для холодильника № {i+1}  '))
#     for j in string:
#         if j == 'a':
#             a = True
#         if j == 'n' and a:
#             n = True
#         if j == 't' and n:
#             t = True
#         if j == 'o' and t:
#             o = True
#         if j == 'n' and o:
#             result.append(i+1)
# print(f'Заражены Холодильники под следующими Номерами: {result} ')
