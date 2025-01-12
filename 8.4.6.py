# Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:
# Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
# Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @ignore_exception, но не код, вызывающий его.

import functools

class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, funcs):
        @functools.wraps(funcs)
        def wrapper(*args, **kwargs):
            try:
                value = funcs(*args, **kwargs)
                return value
            except self.args as err:
                print(f'Исключение {err.__class__.__name__} обработано')
        return wrapper

