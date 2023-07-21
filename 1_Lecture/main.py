"""
n = 1.98
print(n)

n = 'mnnjfwjb'
print(n)

n = 5
print(type(n))

n = 'html'
print(type(n))

"""
# n = 'FDF\'FGF'
# print(n)

# n = 'FDF"777"FGF'
# print(n)

"""
a = 5
b = 5.89
c = 'Hello'

# Печать букв a,b,c
print(a, b, c)
print(a, '-', b, '-', c)

# Печать значений букв a,b,c
print(f"{a} - {b} - {c}")

print("{} - {} - {}".format(a,b,c))

print('Введите первое число')
d = input()
e = input('Введите Второе Число: ')

print(d, '+', e, '=', d + e)

"""
# Приведение типов

#c = 5.89
#print(c)
#n = int(c)
#print(n)

"""
a = 6.9987664
b = 5.0498378

print(round(a*b,3))
#round(1.56567, 2)

"""
"""
iter = 2 
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5
"""

"""
username = input('Введите имя:')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет,', username)
"""
# Программа нахождения минимального делителя числа цикл


"""
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False 
    i += 1
"""
a = 'qwerty'

#print(a[0])

# написание qwerty побуквенно вниз
#for i in a:
#    print (i)

"""
# Цикл 5 раз по 5 * 
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
        print(line)
"""
text = 'Съешь ещё этих Мягких французских булочек'
#print(len(text)) # Кол-во символов в фразе text 41
#print('ещё'in text) # Если есть ещё тогда TRUE
#print(text.lower())
#print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))

# Отрицательное (обратное) индексирование
print(text[-1])
print(text[:])

