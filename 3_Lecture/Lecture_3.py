# def sum_numbers(n, y='Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#         return summa
#     print('Stop')


# a = sum_numbers(5)
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#         return res


# print(sum_str('q', 'e', 'l'))

# РЕКУРСИЯ

# Рекурсия — это функция, вызывающая сама себя.


# Пользователь вводит число n.
# Необходимо вывести n - первых членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих
# 💡 При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]

                                            # Алгоритмы

# Алгоритмом называется набор инструкций для выполнения
# некоторой задачи. В принципе, любой фрагмент программного
# кода можно назвать алгоритмом, но мы с Вами рассмотрим 2
# самых интересных алгоритмы сортировок:
# ● Быстрая сортировка
# ● Сортировка слиянием

# Задача:

# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
# должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном
# порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что
# если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1
# это Иван, который загадал число, друг_2 это Петр, который отгадывает. 

# Итак начнем:
# Иван загадал число 77.
# Петр: Число больше 50? Иван: Да.
# Петр: Число больше 75? Иван: Да.
# Петр: Число больше 87? Иван: Нет.
# Петр: Число больше 81? Иван: Нет.
# Петр: Число больше 78? Иван: Нет.
# Петр: Число больше 76? Иван: Да
# Число оказалось в диапазоне 76 < x < 78, значит это число 77. Задача решена. На
# самом деле мы сейчас познакомились с алгоритмом бинарного поиска, который
# также принадлежит стратегии “разделяй и властвуй”. Давайте перейдем к
# обсуждению программного кода быстрой сортировки.


# ● Быстрая сортировка списком значений

# def quick_sort(array):  # array - массив
#     if len(array) < 1:  # если длина массива меньше 1,
#         return array
#     else:
#         pivot = array[0] # переменная pivot куда мы создаем свой массив
#         less = [i for i in array[1:] if i <= pivot] #1-й массив - цикл по i, берутся все элементы которые <= переменной pivot
#         greater = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)


# print(quick_sort([10, 5, 2, 3]))


# ● Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#                 k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#     nums = [38, 27, 43, 3, 9, 82, 10]
#     merge_sort(nums)
#     print(nums)
