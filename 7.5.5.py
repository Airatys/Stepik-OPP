# Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона, причем a <= b.
# Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 1, 2, 3 и 4.
# Реализуйте класс CustomRange, описывающий последовательность, элементами которой являются одиночные целые числа и числа из определенных диапазонов.
# При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является одиночным целым числом либо диапазоном.
# При передаче экземпляра класса CustomRange в функцию len() должно возвращаться количество элементов в нем.
# При передаче экземпляра класса CustomRange в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса CustomRange, расположенные в обратном порядке.
# Экземпляр класса CustomRange должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
# Помимо этого, экземпляр класса CustomRange должен поддерживать операцию проверки на принадлежность с помощью оператора in.
# Наконец, экземпляр класса CustomRange должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных
# Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
# Примечание 2. Реализация класса CustomRange может быть произвольной, то есть требований к наличию определенных атрибутов нет.
# Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

from collections.abc import Sequence

class CustomRange(Sequence):
    def __init__(self, *args):
        self._args = []
        for i in args:
            if isinstance(i, int):
                self._args.append(i)
            if isinstance(i, str):
                a, b = i.split('-')
                self._args.extend(i for i in range(int(a), int(b) + 1))

    def __getitem__(self, key):
        return self._args[key]

    def __len__(self):
        return len(self._args)