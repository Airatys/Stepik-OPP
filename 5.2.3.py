# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     x — координата вектора по оси xx
#     y — координата вектора по оси yy
# Экземпляр класса Vector должен иметь следующее формальное строковое представление:
# Vector(<координата x>, <координата y>)
# И следующее неформальное строковое представление:
# Вектор на плоскости с координатами (<координата x>, <координата y>)
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

