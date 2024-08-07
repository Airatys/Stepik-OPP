# Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:
#     iterable — итерируемый объект
# Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
# Класс Peekable должен иметь один метод экземпляра:
#     peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration.
#     Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

import itertools

class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.flag = True
        self.res = None

    def peek(self, default=StopIteration):
        try:
            if self.flag:
                self.iterable, iter_peek = itertools.tee(self.iterable)
                self.res = next(iter_peek)
                self.flag = False
            if self.res:
                return self.res
        except:
            if default != StopIteration:
                return default
            raise default

    def __iter__(self):
        return self

    def __next__(self):
        self.flag = True
        return next(self.iterable)