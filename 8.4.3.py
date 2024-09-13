# Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float.
# Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргументы должны принадлежать типам int или float
# Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его.

import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if not all(isinstance(i, (int, float)) for i in args) or not all(
                isinstance(i, (int, float)) for i in kwargs.values()):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        value = self.func(*args, **kwargs)
        return value