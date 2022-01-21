"""
    1. Скрипт проверки типов данных, реализованный с помощью функции type()
"""

# type_list = [None, 12345, 0.12345, 'text', False, {'a': 1, 'b': 2}, ['l', 'i', 's', 't'], (1, 2, 3)]
#
# for el in type_list:
#     print(type(el))

"""
    2. Реализация обмена значениями соседних элементов списка (попарно)
        .split подсмотрел у Вас, Спасибо!
"""

# exchange_list = input('Введите элементы списка: ')
# exchange_list = exchange_list.split()
# print(exchange_list)
#
# for i in range(len(exchange_list)):
#     if i % 2 == 0:
#         exchange_list[i], exchange_list[i+1] = exchange_list[i+1], exchange_list[i]
# print(exchange_list)

"""
    3.1 Определение времени года по введеному номеру месяца (Мой первый вариант)
"""

# month = int(input('Введите месяц числом: '))
# dict_month = {1: 'Jun', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
#               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
# list_season = ['Зима', 'Весна', 'Лето', 'Осень']
#
# if 1 <= month <= 12:
#     if month == 1 or month == 2 or month == 12:
#         print(dict_month.get(month), ' это ', list_season[0])
#     elif month in [3, 4, 5]:
#         print(dict_month.get(month), ' это ', list_season[1])
#     elif month in (6, 7, 8):
#         print(dict_month.get(month), ' это ', list_season[2])
#     else:
#         print(dict_month.get(month), ' это ', list_season[3])
# else:
#     print('Вероятно у Вас не стандартный календарь\n'
#           'Поэтому просто используйте арабские цифры от 1 до 12')

"""
    3.2 Определение времени года по введеному номеру месяца (Модернизировано под list типа (winter = [1, 2, 12]))
"""

# month = int(input('Введите месяц числом: '))
# dict_month = {1: 'Jun', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
#               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
#
# winter = [1, 2, 12]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
#
# if month in winter:
#     print('Зима')
# elif month in spring:
#     print('Весна')
# elif month in summer:
#     print('Лето')
# elif month in autumn:
#     print('Осень')
# else:
#     print('Вероятно у Вас не стандартный календарь\n'
#           'Поэтому просто используйте арабские цифры от 1 до 12')

"""
    3.3 Определение времени года по введеному номеру месяца (Протестировано для изучения назначения методов словаря)
"""

# month = int(input('Введите месяц числом: '))
#
# seasons_dict = {}
# seasons_dict = seasons_dict.fromkeys([12, 1, 2], 'Зима')
# seasons_dict.update({}.fromkeys([3, 4, 5], 'Весна'))
# seasons_dict.update({}.fromkeys([6, 7, 8], 'Лето'))
# seasons_dict.update({}.fromkeys([9, 10, 11], 'Осень'))
#
# print(seasons_dict.get(month))

"""
    4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
       Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
       Если слово длинное, выводить только первые 10 букв в слове.
"""

# in_text = input('Введите строку из нескольких слов: ')
# in_text = in_text.split()
# print(in_text)
#
# for i in range(len(in_text)):
#     print(f'{i+1}. {in_text[i][:10]}')

"""
    5. Структура «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. 
       У пользователя запрашивается новый элемент рейтинга. 
       Если в рейтинге существуют элементы с одинаковыми значениями, 
       то новый элемент с тем же значением должен разместиться после них.
"""

# my_list = [7, 5, 3, 3, 2]
# in_number = int(input('Введите число: '))
# for i in range(len(my_list)):
#     if in_number >= my_list[i]:
#         my_list.insert(i, in_number)
#         break
# else:
#     my_list.append(in_number)
#
# print(my_list)

"""
    6. Не успеваю! Добавлю в следующее задание и помечу в комментарии.
"""