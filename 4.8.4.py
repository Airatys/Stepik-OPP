# Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:
#     birth_date — дата рождения, представленная в одном из следующих вариантов:
#     экземпляр класса date
#     строка с датой в ISO формате
#     список или кортеж из трех целых чисел: года, месяца и дня
# Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Экземпляр класса BirthInfo должен иметь один атрибут:
#     birth_date — дата рождения в виде экземпляра класса date
# Класс BirthInfo должен иметь одно свойство:
#     age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день
# Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.
# Приведенный ниже код:
# birthinfo = BirthInfo(date(2023, 2, 26))
# print(birthinfo.age)
# в 2024-02-25 должен выводить:
# 0
# в 2024-02-26 должен выводить:
# 1
# в 2025-02-25 должен выводить:
# 1
#  в 2025-02-26 должен выводить:
# 2
# Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.
# Примечание 3. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.

import re
from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _date(self, birth_date):
        try:
            txt = re.fullmatch(r'\b\d{4}-\d{2}-\d{2}\b', birth_date)
            b = map(int, txt.group().split('-'))
            self.birth_date = date(*b)
        except:
            raise TypeError ('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def _date(self, birth_date):
        try:
            a, b, c = birth_date
            self.birth_date = date(a, b, c)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age
    
    
