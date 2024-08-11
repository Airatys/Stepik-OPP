# Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является последовательностью.
# Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи.
# Объединение должно происходить аналогично тому, как это делает функция zip().
# При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.
# Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
# Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.
# Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
# Примечание 2. Экземпляр класса SequenceZip не должен зависеть от последовательностей, на основе которых он был создан.
# Другими словами, если исходные последовательности изменятся, то экземпляр класса SequenceZip измениться  не должен.
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.

from copy import deepcopy

class SequenceZip:
    def __init__(self, *args):
        self.myzip = deepcopy(zip(*args))

    def __len__(self):
        return sum(1 for _ in deepcopy(self.myzip))

    def __getitem__(self, item):
        for key, value in enumerate(deepcopy(self.myzip)):
            if key == item:
                return value

    def __iter__(self):
        yield from deepcopy(self.myzip)



# from copy import copy
#
# class SequenceZip:
#     def __init__(self, *args):
#         self.myzip = copy([i for i in zip(*args)])
#
#     def __len__(self):
#         return len(self.myzip)
#
#     def __getitem__(self, item):
#         if not isinstance(item, int):
#             raise TypeError
#         if item < 0 or item >= len(self.myzip):
#             raise IndexError
#         return self.myzip[item]
#
#     def __iter__(self):
#         yield from self.myzip