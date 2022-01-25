"""
    1. Реализовать функцию, принимающую два числа (позиционные аргументы)
    и выполняющую их деление.
    Числа запрашивать у пользователя,
    предусмотреть обработку ситуации деления на ноль.
"""


# def my_func():
#     try:
#         var_1 = float(input('Первое число: '))
#         var_2 = float(input('Второе число: '))
#     except ValueError:
#         return
#     split = var_1 / var_2 if var_2 != 0 else 'var_2 != 0'
#     return split
#
#
# split = my_func()
# print(split)

"""
    2. Выполнить функцию, которая принимает несколько параметров, 
    описывающих данные пользователя: 
    имя, фамилия, год рождения, город проживания, email, телефон. 
    Функция должна принимать параметры как именованные аргументы. 
    Осуществить вывод данных о пользователе одной строкой.
"""


# def user_func(**kwargs):
#     return kwargs
#
#
# print(user_func(name='Greg', lastname='Kotelnikov', year_of_birth=1996, city='Volgograd',
#                 email='kotelgreg@gmail.com', phone_number='+7-999-999-99-99'))

"""
    3. Реализовать функцию my_func(), 
    которая принимает три позиционных аргумента 
    и возвращает сумму наибольших двух аргументов.
"""


# def my_func(var_1, var_2, var_3):
#
#     my_list = [var_1, var_2, var_3]
#     # for i in range(my_list(lvl)-1):
#     #     if my_list[i] <= my_list[i+1]:
#     #         my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
#     # if my_list[0] < my_list[1]:
#     #     my_list[0], my_list[1] = my_list[1], my_list[0]
#
#     my_list.sort(reverse=True)
#     sum = my_list[0] + my_list[1]
#     return sum
#
#
#  print(my_func(5, 3, 10))

"""
    4.1 Программа принимает действительное положительное число x 
    и целое отрицательное число y. Выполните возведение числа x в степень y. 
    Задание реализуйте в виде функции my_func(x, y). 
    При решении задания нужно обойтись без встроенной функции возведения числа в степень.
    
    Первый — возведение в степень с помощью оператора **.
"""


# my_func = lambda x, y: x ** y
#
# print(my_func(5, -1))


# def my_func(x: float, y: int):
#     if x > 0:
#         x **= y if y < 0 else print('Введите данные, согласно условию')
#     else:
#         print('Введите данные, согласно условию')
#     return x
#
#
# print(my_func(10, -10))


"""
    4.2 Программа принимает действительное положительное число x 
    и целое отрицательное число y. Выполните возведение числа x в степень y. 
    Задание реализуйте в виде функции my_func(x, y). 
    При решении задания нужно обойтись без встроенной функции возведения числа в степень.
    
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# def my_func(x: float, y: int):
#     if x > 0:
#         if y < 0:
#             num = 1
#             while y < 0:
#                 num /= x
#                 y += 1
#         else:
#             print('Введите данные, согласно условию')
#     else:
#         print('Введите данные, согласно условию')
#     return num
#
#
# print(my_func(10.15, -2))

"""
    5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
    При нажатии Enter должна выводиться сумма чисел. 
    Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
    Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается. 
    Если специальный символ введён после нескольких чисел, 
    то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
    и после этого завершить программу.
"""


# def sum_num(in_str):
#     in_list = in_str.split()
#     my_sum = 0
#     for el in in_list:
#         if el:
#             try:
#                 if el == "N":
#                     return my_sum, False
#                 else:
#                     my_sum += int(el)
#             except ValueError:
#                 continue
#     return my_sum, True
#
#
# continue_flag = True
# result_sum = 0
# while continue_flag:
#     in_str = input('Введите числа через пробел. для остановки введите N: ')
#     current_sum, continue_flag = sum_num(in_str)
#     result_sum += current_sum
#     print(result_sum)
# print(result_sum)


"""
    6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв 
    и возвращающую их же, но с прописной первой буквой. 
    Например, print(int_func(‘text’)) -> Text.
"""


# def int_func(in_str):
#     in_list = in_str.split()
#     for word in in_list:
#         result_word = ''
#         split_word = list(word)
#         f_sim = ord(split_word[0])
#         if 97 <= f_sim <= 122:
#             split_word.pop(0)
#             split_word.insert(0, chr(f_sim - 32))
#         for i in range(len(split_word)):
#             result_word = result_word + split_word[i]
#         print(result_word)
#     return
#
#
# print(int_func('text GREG'))

"""
    7. Продолжить работу над заданием. 
    В программу должна попадать строка из слов, разделённых пробелом. 
    Каждое слово состоит из латинских букв в нижнем регистре. 
    Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
    Используйте написанную ранее функцию int_func().
    
    Случайно сделал в предыдущем задании, но слегка доработал с выводом в строку.
"""


# def int_func(in_str):
#     in_list = in_str.split()
#     result_str = ''
#     for word in in_list:
#         split_word = list(word)
#         f_sim = ord(split_word[0])
#         if 97 <= f_sim <= 122:
#             split_word.pop(0)
#             split_word.insert(0, chr(f_sim - 32))
#         for i in range(len(split_word)):
#             result_str = result_str + split_word[i]
#         result_str = result_str + ' '
#     print(result_str)
#     return
#
#
# print(int_func('text Alyona'))