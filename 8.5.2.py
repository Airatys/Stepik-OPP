# Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса, является объектом типа mappingproxy, а не dict.
# Приведенный ниже код:
# class MyClass:
#     pass
# print(type(MyClass.__dict__))
# выводит:
# <class 'mappingproxy'>
# Тип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством методов, а главное — отсутствием магического метода __setitem__().
# Это значит, в объект типа mappingproxy нельзя напрямую добавить новую пару ключ-значение, а также изменить значение имеющегося ключа.
# Приведенный ниже код:
# class MyClass:
#     pass
# MyClass.__dict__['__doc__'] = 'docstring'
# приводит к возбуждению исключения:
# TypeError: 'mappingproxy' object does not support item assignment
# Для добавления классу необходимого атрибута можно использовать функцию setattr().
# Приведенный ниже код:
# class MyClass:
#     pass
# setattr(MyClass, '__doc__', 'docstring')
# print(MyClass.__doc__)
# выводит:
# docstring
# Реализуйте декоратор @add_attr_to_class для декорирования класса.
# Декоратор должен принимать произвольное количество именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.

def add_attr_to_class(**attr):
    def decorator(cls):
        for k, v in attr.items():
            setattr(cls, k, v)
        return cls
    return decorator
