"""
    1. Создать класс TrafficLight (светофор).
    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд,
    второго (жёлтый) — 2 секунды,
    третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов.
    При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
# from time import sleep
# from itertools import cycle
#
#
# class TrafficLight:
#     colors_light = ("Красный", "Желтый", "Зеленый")
#     delay_time = (7, 2, 3)
#
#     def __init__(self, color):
#         self.__color = color
#
#     def running(self):
#         col_cycle = cycle(self.colors_light)
#         for col in col_cycle:
#             if self.__color == col:
#                 print(col)
#                 sleep(self.delay_time[self.colors_light.index(self.__color)])
#                 # sleep(3)
#                 self.__color = next(col_cycle)
#
#
# t = TrafficLight("Желтый")
# t.running()

"""
    2. Реализовать класс Road (дорога).
    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
    толщиной в 1 см*число см толщины полотна;
    проверить работу метода.
    Например: 20 м*5000 м*25 кг*5 см = 125000 т.
"""


# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     @property
#     def sq(self):
#         return self._length * self._width
#
#     def mass_asph(self, mass_m, thickness):
#         mass = self.sq * mass_m * thickness
#         return mass
#
#
# road = Road(5000, 20)
# print(f'{road.sq} - площадь дороги\n'
#       f'{road.mass_asph(25, 0.05)} - масса асфальта')

"""
    3. Реализовать базовый класс Worker (работник).
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
    оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
    и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, 
    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


# class Worker:
#
#     def __init__(self, name, surname, position , wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     @property
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     @property
#     def get_total_income(self):
#         return self._income["wage"] + self._income["bonus"]
#
#
# pos = Position("Greg", "Kotelnikov", "Systems Analyst", 35000, 5000)
# print(pos.get_full_name, pos.get_total_income)


"""
    4. Реализуйте базовый класс Car.
    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, 
    что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. 
    Выполните доступ к атрибутам, выведите результат. 
    Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} {self.color} {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула на {direction}')

    def show_speed(self):
        print(f'Скорость - {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            super().show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        else:
            super().show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name,  is_police=True)


racer = SportCar(100, "Синий", "Nissan JUKE")
racer.go()
police = PoliceCar(110, "Белый", "Toyota CAMRY")
police.turn("право")
worker = WorkCar(100, "Синий", "Nissan JUKE", False)
worker.show_speed()

