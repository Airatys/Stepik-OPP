# Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     iterable — итерируемый объект
#     n — целое неотрицательное число
# Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

class SkipIterator:
    def __init__(self, iterable, n) -> None:
        self.iterable = list(iterable)
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            for i in self.iterable:
                res = self.iterable[self.index]
                self.index += self.n + 1
                return res
        except:
            raise StopIteration