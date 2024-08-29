# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры:

class Shape:
    pass


class Polygon(Shape):
    pass


class Circle(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Quadrilateral):
    pass


class Square(Quadrilateral):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass
