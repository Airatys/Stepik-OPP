# Реализуйте класс данных Point, описывающий точку на координатной плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     x — координата точки по оси x (тип float), по умолчанию имеет значение 0.0
#     y — координата точки по оси y (тип float), по умолчанию имеет значение 0.0
# Экземпляр класса Point должен иметь три атрибута:
#     x — координата точки по оси x
#     y — координата точки по оси y
#     quadrant — координатная четверть, к которой принадлежит точка (тип int). Если точка лежит на одной из осей, координатная четверть считается равной 0
# Класс Point должен иметь два метода экземпляра:
#     symmetric_x() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси x
#     symmetric_y() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси y
# Экземпляр класса Point должен иметь следующее формальное строковое представление:
# Point(x=<координата x>, y=<координата y>, quadrant=<координатная четверть>)
# Наконец, экземпляры класса Point должны поддерживать между собой операцию сравнения с помощью операторов == и !=.
# Две точки считаются равными, если их координаты по обеим осям совпадают.
# Примечание 1. Для точки с координатами (x,y)(x,y) симметричной относительно оси xx будем считать точку с координатами (x,−y)(x,−y), симметричной относительно оси y — точку с координатами (−x,y)(−x,y).

from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, default=0)

    def __post_init__(self):
        if self.x == 0.0 or self.y == 0.0:
            self.quadrant = 0
        elif self.x < 0.0 and self.y > 0.0:
            self.quadrant = 2
        elif self.x > 0.0 and self.y > 0.0:
            self.quadrant = 1
        elif self.x < 0.0 and self.y < 0.0:
            self.quadrant = 3
        else:
            self.quadrant = 4

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)
