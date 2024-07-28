# Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.
# Примечание 1. Числами будем считать экземпляры классов int и float.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.

class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, (int, float)):
                object.__setattr__(self, k, abs(v))
            else:
                object.__setattr__(self, k, v)

 # Базовая реализация setattr и через реализацию своего метода.

class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            self.__dict__[key] = abs(value)
        else:
            self.__dict__[key] = value


