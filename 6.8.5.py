# Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое число в заданном диапазоне.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#     start — целое число
#     end — целое число
#     cache — булево значение, по умолчанию равняется False
# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
# При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно.
# Если в качестве значения параметра cache при создании дескриптора было указано значение True, при каждом обращении к атрибуту дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.
# При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:
# Изменение невозможно
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса RandomNumber нет, она может быть произвольной.

from random import randint

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.gen = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.cache and self.gen is None:
            self.gen = randint(self.start, self.start)
            return self.gen
        else:
            self.gen = randint(self.start, self.start)
            return self.gen

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')

