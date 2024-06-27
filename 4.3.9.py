# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     x — координата вектора по оси xx, по умолчанию имеет значение 0
#     y — координата вектора по оси yy, по умолчанию имеет значение 0
# Экземпляр класса Vector должен иметь два атрибута:
#     x — координата вектора по оси xx
#     y — координата вектора по оси yy
# Класс Vector должен иметь один метод экземпляра:
#     abs() — метод, возвращающий модуль вектора
# Примечание 1. Модуль вектора с координатами (x,y)(x,y) вычисляется по формуле x2+y2x2+y2
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2)