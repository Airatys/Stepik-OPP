# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.
# Класс Processor имеет один статический метод:
#     process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат.
#     Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
#     Аргумент переданного типа не поддерживается
# Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.
# Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.
# Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.

from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    def _process(data: int | float):
        return data * 2
    
    @process.register
    def _proceess(data: str):
        return data.upper()
    
    @process.register
    def _process(data: list):
        return sorted(data)
    
    @process.register
    def _process(data: tuple):
        return tuple(sorted(data))
    
        