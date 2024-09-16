# Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:
# a = Vector(1, 2, 3)
# b = Vector(3, 4, 5)
# c = Vector(5, 6, 7, 8)
# В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:
# print(a)                       # (1, 2, 3)
# print(b)                       # (3, 4, 5)
# print(c)                       # (5, 6, 7, 8)
# Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:
# print(a + b)                   # (4, 6, 8)
# print(a - b)                   # (-2, -2, -2)
# print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
# print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
# а также операции сравнения на равенство и неравенство:
# print(a == Vector(1, 2, 3))    # True
# print(a == Vector(4, 5, 6))    # False
# При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:
# Векторы должны иметь равную длину

from functools import total_ordering
import math

@total_ordering
class Vector:
    def __init__(self, *args: tuple):
        self.vec = args

    def __str__(self):
        return f'{self.vec}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__class__.check_len(self.vec, other.vec):
                return (self.vec) == (other.vec)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.__class__.check_len(self.vec, other.vec):
                return (self.vec) < (other.vec)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.__class__.check_len(self.vec, other.vec):
                return Vector(*(i+j for i, j in zip(self.vec, other.vec)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.__class__.check_len(self.vec, other.vec):
                return Vector(*(i-j for i, j in zip(self.vec, other.vec)))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self.__class__.check_len(self.vec, other.vec):
                return sum(i*j for i, j in zip(self.vec, other.vec))
        return NotImplemented

    def norm(self):
        return math.sqrt(sum(i**2 for i in self.vec))

    @staticmethod
    def check_len(obj_a, obj_b):
        if len(obj_a) == len(obj_b):
            return True
        raise ValueError('Векторы должны иметь равную длину')

