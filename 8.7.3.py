# Реализуйте класс AttributesMixin, добавляющий классам функционал получения информации об атрибутах их экземпляров.
# Класс AttributesMixin должен иметь два метода экземпляра:
#     get_public_attributes() — метод, возвращающий список имен и значений публичных атрибутов экземпляров класса, которому добавляется функционал
#     get_protected_attributes() — метод, возвращающий список имен и значений защищенных атрибутов экземпляров класса, которому добавляется функционал
# Списки, возвращаемые методами get_public_attributes() и get_protected_attributes(), должны иметь следующий формат:
# [(<имя атрибута>, <значение атрибута>), (<имя атрибута>, <значение атрибута>), ...]
# Примечание 1. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса AttributesMixin нет, она может быть произвольной.

class AttributesMixin:
    def get_public_attributes(self):
        mylist = []
        for i in self.__dict__.items():
            if not i[0].startswith('_'):
                mylist.append(i)
        return mylist

    def get_protected_attributes(self):
        mylist = []
        for i in self.__dict__.items():
            if i[0].startswith('_') and i[0].count('_') < 3:
                mylist.append(i)
        return mylist


