# Квадратный трехчлен — это многочлен вида ax2+bx+cax2+bx+c, где a≠0a=0. Например:
# x2+1x2−5x+6
# x2+1x2−5x+6Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#     a — коэффициент aa квадратного трехчлена
#     b — коэффициент bb квадратного трехчлена
#     c — коэффициент cc квадратного трехчлена
# Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
#     a — коэффициент aa квадратного трехчлена
#     b — коэффициент bb квадратного трехчлена
#     c — коэффициент cc квадратного трехчлена
# Класс QuadraticPolynomial должен иметь два метода класса:
#     from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c, которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов
#     from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c квадратного трехчлена, записанные через пробел.
# Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float 
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    @classmethod
    def from_iterable(cls, iterabl):
        a, b, c = iterabl
        return cls(a, b, c)
     
    @classmethod    
    def from_str(cls, string):
        a, b, c = map(float, string.split())
        return cls(a, b, c)
