"""
    1. Реализовать класс «Дата»,
    функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.

"""


# class Date:
#     def __init__(self, date):
#         self.date = date #dd_mm_yyyy
#
#     # def extract_data(self):
#     #     try:
#     #         day, month, year = self.date.split()
#     #         return day, month, year
#     #     except Exception as e:
#     #         print(f"Не удалось выделить дату из строки {e}")
#
#     @staticmethod
#     def validate_data(date_in):
#         try:
#             day, month, year = date_in.split()
#             if int(day) not in range(1, 32):
#                 raise ValueError("День указан некорректно")
#             elif int(month) not in range(1, 13):
#                 raise ValueError("Месяц указан некорректно")
#             elif int(year) not in range(0, 2100):
#                 raise ValueError("Год указан некорректно")
#         except ValueError as e:
#             print(e)
#         else:
#             print(f"Дата успешно провалидированна: {int(day):02d}-{int(month):02d}-{year}")
#
#
# # d = {day: 30, month: 3, year: 2005}
# # d = Date('20 02 2022')
# # my_date = d.extract_data()
# # print(my_date)
# # if my_date:
# #     d.validate_data(my_date)
# print(Date.validate_data("20 2 2022"))


"""
    2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
    Проверьте его работу на данных, вводимых пользователем. 
    При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


# class ZeroError(Exception):
#     def __init__(self):
#         self.text = "Делить на ноль нельзя (нет)"
#
#
# def check_num(a, b):
#     try:
#         if b == 0:
#             raise ZeroError
#         print(a / b)
#     except ZeroError as err:
#         print(err.text)
#
#
# check_num(20, 0)


"""
    3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
    Проверить работу исключения на реальном примере. 
    Запрашивать у пользователя данные и заполнять список необходимо только числами. 
    Класс-исключение должен контролировать типы данных элементов списка.
    Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
    пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
    При этом скрипт завершается, сформированный список с числами выводится на экран.
    Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
    Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
    Вносить его в список, только если введено число. 
    Класс-исключение должен не позволить пользователю ввести текст (не число) 
    и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""

#
# class My_exception(Exception):
#     def __init__(self):
#         self.text = 'Нужно ввести число!'
#
#
# my_list = []
# in_num = input('Что бы остановить, напиши "stop". Введите число: ')
# while in_num:
#     try:
#         if in_num.isdigit():
#             my_list.append(float(in_num))
#         elif in_num == 'stop':
#             break
#         else:
#             raise My_exception
#     except My_exception as e:
#         print(e.text)
#     in_num = input('Что бы остановить, напиши "stop". Введите число: ')
# print(my_list)

"""
        4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
    А также класс «Оргтехника», который будет базовым для классов-наследников. 
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
    В базовом классе определите параметры, общие для приведённых типов. 
    В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
        5. Продолжить работу над первым заданием. 
    Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
    Для хранения данных о наименовании и количестве единиц оргтехники, 
    а также других данных, можно использовать любую подходящую структуру (например, словарь).
        6. Продолжить работу над вторым заданием. 
    Реализуйте механизм валидации вводимых пользователем данных. 
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Недостаточно техники на складе.")
        except KeyError:
            print("Такого типа техники на складе нет.")
    return wrapper

class Storage:
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]["count"] -= unit_count

    @classmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Неверный формат входных данных!")
        else:
                self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model["count"] += self.__count
            else:
                equipment_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            equipment_storage_info[self.name] = {
                self.model: {"count": self.__count}
            }

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(self, name, model, "Printer", count)
        self.colors = colors


class Laptop(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(self, name, model, "Printer", count)
        self.ram = ram
        self.system_type = system_type


printer1 = Printer("HP", 'XC111', 100, '"red", "green", "blue"')
printer2 = Printer("Canon", 'TT551', 200, ["black"])

Storage.get_all_equipment()
"""
    7. Реализовать проект «Операции с комплексными числами». 
    Создайте класс «Комплексное число». 
    Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
    Проверьте работу проекта. 
    Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
    Проверьте корректность полученного результата.
"""
