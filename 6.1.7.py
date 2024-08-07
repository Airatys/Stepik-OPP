# Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
#     iterable — итерируемый объект
# Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
# Класс LoopTracker должен иметь четыре свойства:
#     accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент
#     empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора
#     first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его.
#     Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение AttributeError с текстом:
#     Исходный итерируемый объект пуст
#     last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент.
#     Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
#     Последнего элемента нет
# Класс LoopTracker должен иметь один метод экземпляра:
#     is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

from copy import copy

class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.iter_copy = copy(self.iterable)
        self.iter_end = None
        self.count_1 = 0
        self.count_2 = 0

    @property
    def accesses(self):
        return self.count_1

    @property
    def empty_accesses(self):
        return self.count_2

    @property
    def first(self):
        try:
            iter_first = copy(self.iter_copy)
            obj_first = next(iter_first)
            return obj_first
        except:
            self.count_2 += 1
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.count_1 == 0:
            raise AttributeError('Последнего элемента нет')
        return self.iter_end

    def is_empty(self):
        try:
            iter_is_empty = copy(self.iterable)
            next(iter_is_empty)
            return False
        except:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.iter_end = next(self.iterable)
            self.count_1 += 1
            return self.iter_end
        except:
            self.count_2 += 1
            raise





