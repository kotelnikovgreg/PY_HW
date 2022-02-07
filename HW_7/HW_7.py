"""
    1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
    (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин,
    расположенных в виде прямоугольной схемы.
    Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

    31    32         3    5    32        3    5    8    3
    37    43         2    4    6         8    3    7    1
    51    86        -1   64   -8

    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения
    двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
    первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         m_str = '\n'
#         for row in self.matrix:
#             for el in row:
#                 m_str += f'|{el:>5}'
#             m_str += '|\n'
#         return m_str
#
#     def __add__(self, other):
#         add = []
#         if len(self.matrix) != len(other.matrix):
#             print("Размерность матриц не совпадает")
#             return
#         for i in range(len(self.matrix)):
#             row = []
#             if len(self.matrix[i]) != len(other.matrix[i]):
#                 print("Размерность матриц не совпадает")
#                 return
#             for j in range(len(self.matrix[i])):
#                 row.append(self.matrix[i][j] + other.matrix[i][j])
#             add.append(row)
#         return Matrix(add)
#
#
# m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
# m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 0]])
# print(f'{m1}          + {m2}          = {m1 + m2}')

"""
    2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
    Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
    К типам одежды в этом проекте относятся пальто и костюм. 
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: 
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
    Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. 
    Проверить на практике полученные на этом уроке знания: 
    реализовать абстрактные классы для основных классов проекта, 
    проверить на практике работу декоратора @property.
"""


# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     def __init__(self, dimension):
#         self.dimension = dimension
#
#     @abstractmethod
#     def consumption(self):
#         pass
#
#
# class Coat(Clothes):
#     def __init__(self, dimension):
#         # self.dimension = dimension
#         # try:
#         #     for dimen in range(44, 55):
#         #         if dimen == self.dimension:
#         #             raise ("num shold be in range 44 - 55")
#         # except TypeError:
#         #     print('Check num value')
#         super().__init__(dimension)
#
#
#
#     @property
#     def consumption(self):
#         return round(self.dimension / 6.5 + 0.5, 2)
#
#
# class Costume(Clothes):
#     def __init__(self, dimension):
#         # dimen_num = range(1.43, 2.01)
#         # for dimen in dimen_num:
#         #     if self.dimension != dimen:
#         #         print("Indicate size by number in range 143 - 179")
#         #     else:
#         super().__init__(dimension)
#
#     @property
#     def consumption(self):
#         return round(self.dimension * 2 + 0.3, 2)
#
#
# coat = Coat(50)
# print(f'Consumtion for coat - {coat.consumption}')
# costume = Costume(1.78)
# print(f'Consumtion for costume - {costume.consumption}')


"""
    3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 
    Необходимо создать класс Клетка. 
    В его конструкторе инициализировать параметр, 
    соответствующий количеству ячеек клетки (целое число). 
    В классе должны быть реализованы методы перегрузки арифметических операторов: 
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). 
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
    умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
    Сложение. Объединение двух клеток. 
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    Вычитание. Участвуют две клетки. 
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
        иначе выводить соответствующее сообщение.
    Умножение. Создаётся общая клетка из двух. 
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    Деление. Создаётся общая клетка из двух. 
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
    Данный метод позволяет организовать ячейки по рядам.
    Метод должен возвращать строку вида *****\n*****\n*****..., 
    где количество ячеек между \n равно переданному аргументу. 
    Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернёт строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернёт строку: *****\n*****\n*****.
    Подсказка: подробный список операторов для перегрузки доступен по ссылке.
    """


class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('num should be > 0')
            self.num = int(num)
        except TypeError:
            self.num = 1
            print('Check num value')
        except ValueError:
            print('Check num value')
            self.num = 1

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Substraction is impossible')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell_1 = Cell(100)
cell_2 = Cell(100)
print(cell_1.make_order(10))
print()
print(cell_2.make_order(4))