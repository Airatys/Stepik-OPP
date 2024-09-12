# Реализуйте класс декоратор @limited_calls, который принимает один аргумент:
#     n — целое число
# Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз, должно быть возбуждено исключение MaxCallsException с текстом:
# Превышено допустимое количество вызовов
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @limited_calls, но не код, вызывающий его.

from functools import wraps

class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.n):
                self.count += 1
                if self.count > self.n:
                    raise MaxCallsException('Превышено допустимое количество вызовов')
                value = func(*args, **kwargs)
                return value
        return wrapper

