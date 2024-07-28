# Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции. Счетчик вызовов должен быть доступен по атрибуту calls.
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CountCalls, но не код, вызывающий его.

class CountCalls:
    calls = 0
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)