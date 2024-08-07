# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#     proteins — количество белков в граммах
#     fats — количество жиров в граммах
#     carbohydrates — количество углеводов в граммах
# Экземпляр класса FoodInfo должен иметь три атрибута:
#     proteins — количество белков в граммах
#     fats — количество жиров в граммах
#     carbohydrates — количество углеводов в граммах
# И следующее формальное строковое представление:
# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
# Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.
# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью операторов *, / и // соответственно:
#     результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого умножены на n
#     результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены на n
#     результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены нацело на n
# Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.
# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
# Примечание 3. Никаких ограничений касательно реализации класса FoodInfo нет, она может быть произвольной.

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented


