# Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
# Экземпляр класса AttrsNumberObject должен иметь один атрибут:
#     attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.

class AttrsNumberObject:
    def __init__(self, attrs_num = 0, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = attrs_num

    def __getattribute__(self, item):
        if item == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, item)