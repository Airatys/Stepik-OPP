# Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Formatter должен иметь один статический метод:
#     format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа.
# Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
#     Аргумент переданного типа не поддерживается
# Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.
# Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.

from functools import singledispatchmethod

class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
     
    @format.register(int)    
    def _format(data):
        print(f'Целое число: {data}')
        
    @format.register(float)    
    def _format(data):
        print(f'Вещественное число: {data}')
    
    @format.register(tuple)    
    def _format(data):
        print(f'Элементы кортежа: {', '.join([str(i) for i in data])}')
    
    @format.register(list)    
    def _format(data):
        print(f'Элементы списка: {', '.join([str(i) for i in data])}')
    
    @format.register(dict)    
    def _format(data):
        print(f'Пары словаря: {', '.join(map(str, data.items()))}')




