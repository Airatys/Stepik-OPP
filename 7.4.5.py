from collections import UserList

class NumberList(UserList):
    @staticmethod
    def int_digit(digit):
        if isinstance(digit, (int, float)):
            return digit
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __init__(self, iterable):
        super().__init__(self.int_digit(i) for i in iterable)

    def __setitem__(self, key, value):
        self.data.__setitem__(key, self.int_digit(value))

    def append(self, item):
        self.data.append(self.int_digit(item))

    def extend(self, other):
        self.data.extend(self.int_digit(i) for i in other)

    def __iadd__(self, other):
        return self.data + [self.int_digit(i) for i in other]