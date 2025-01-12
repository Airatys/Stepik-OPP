# Реализуйте класс MROHelper, описывающий набор функций для работы с MRO произвольных классов. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс MROHelper должен иметь три статических метода:
#     len() — метод, принимающий в качестве аргумента класс и возвращающий количество элементов в его MRO
#     class_by_index() — метод, принимающий в качестве аргументов класс cls и целое число n, по умолчанию равное нулю, и возвращающий класс с индексом n в MRO класса cls
#     index_by_class() — метод, принимающий в качестве аргументов два класса child и parent и возвращающий целое число — индекс класса parent в MRO класса child
# Примечание 1. Нумерация классов в MRO начинается с нуля.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Никаких ограничений касательно реализации класса MROHelper нет, она может быть произвольной.

class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)

