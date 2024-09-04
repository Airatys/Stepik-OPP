# Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа.
# При создании экземпляра класс должен принимать один аргумент:
#     iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList.
#     Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
#     Элементами экземпляра класса NumberList должны быть числа
#     Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
# При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:
# Элементами экземпляра класса NumberList должны быть числа
# Примечание 1. Числами будем считать экземпляры классов int и float.
# Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.

from collections import UserList

class NumberList(UserList):
    @staticmethod
    def int_digit(digit):
        if isinstance(digit, (int, float)):
            return digit
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __init__(self, iterable=()):
        super().__init__(self.int_digit(i) for i in iterable)

    def __setitem__(self, key, value):
        self.data.__setitem__(key, self.int_digit(value))

    def append(self, item):
        self.data.append(self.int_digit(item))

    def extend(self, other):
        self.data.extend(self.int_digit(i) for i in other)

    def insert(self, index, item):
        self.data.insert(index, self.int_digit(item))

    def __iadd__(self, other):
        return self.data + [self.int_digit(i) for i in other]

