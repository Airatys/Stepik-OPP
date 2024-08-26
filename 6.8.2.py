# Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута является неотрицательным целым числом.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     name — имя атрибута, за которым будет закреплен дескриптор
#     default — значение по умолчанию. Если не передан, имеет значение None
# При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора.
# Если значение по умолчанию равняется None, должно быть возбуждено исключение AttributeError с текстом:
# Атрибут не найден
# При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным целым числом.
# Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с текстом:
# Некорректное значение
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной.

class NonNegativeInteger:
    def __init__(self, name, default=None):
        self.name = name
        self.default = default
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            if self.default is None:
                raise AttributeError('Атрибут не найден')
            return self.default

    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Некорректное значение')
