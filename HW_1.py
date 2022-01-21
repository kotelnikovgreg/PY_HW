#1

# my_name = 'GREG'
# age = 25
# c = [1, 2, 'Hello, Sasha!']
#
# print(c[2],
#      '\nMy name is', my_name,
#      '\nIm', age, 'years old')
#
# number = input('Введите число: ')
# string = input('Введите текст: ')
# print('Введенное число - ', number,
#       '\nВведенная строка - ', string)

#2

# sec_in = int(input('Введите кол-во секунд: '))
# hh = sec_in // 3600
# mm = sec_in % 3600 // 60
# ss = sec_in % 3600 % 60
# print(f'В формате чч:мм:сс - {hh:02d}:{mm:02d}:{ss:02d}')

#3

# n = int(input('Введите целое число: '))
# nn = int(str(n) * 2)
# nnn = int(str(n) * 3)
# result = n + nn + nnn
# print(f"n + nn + nnn = {n} + {nn} + {nnn} = {result}")

#4

# Хочу что бы пользователь мог вводить любое число и получать обратную связь,
# поэтому решил пойти через float

# Слишком большое число прошу не вводить, потому как он пишет
# в формате (2.123e+22)

# int_num = float(input('Введите целое, положительное число: '))
# if int_num >= 1:
#     if int(int_num)/float(int_num) == 1:
#         int_num = str(int_num)
#         numbers = list(int_num)
#         print(numbers)
# else:
#     print('Введите нормальное число!')
# i = 0
# max = numbers[0]
# # Определиляю индекс последнего элемента для цикла
# # print(len(numbers)-3)
# while i <= (len(numbers)-3):
#     if numbers[i] > max:
#          max = numbers[i]
#          # Просматриваю работу цикла
#          # print(max)
#     i += 1
# print(f'Самая большая цифра в числе - {max}')

#5

# revenue = float(input('Введите выручку: '))
# outgo = float(input('Введите издержки: '))
# if revenue > outgo:
#     profit = revenue - outgo
#     profitability = profit / revenue
#     emp = int(input('Введите количество сотрудников: '))
#     profit_for_emp = profit / emp
#     print(f'Прибыль — выручка больше издержек \n '
#           f'Рентабельность - {profitability}\n'
#           f'Прибыль на одного сотрудника - {profit_for_emp}')
# else:
#     print('Убыток — издержки больше выручки')

#6

# a = float(input('Введите кол-во км в первый день: '))
# b = float(input('Результат спортсмена км: '))
# day = 1
# while a < b:
#     print(f'{day}-й день: {a:.2f}')
#     a *= 1.1
#     day += 1
# print(f'{day}-й день: {a:.2f}')
# print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км')