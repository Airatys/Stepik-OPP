# Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении.
# При создании экземпляра класс должен принимать один аргумент:
#     iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
# Класс SortedList должен иметь три метода экземпляра:
#     add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
#     discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
#     update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
# Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.
# Экземпляр класса SortedList должен иметь следующее формальное строковое представление:
# SortedList([<первый элемент списка>, <второй элемент списка>, ...])
# При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем.
# При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.
# Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
# Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.
# Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
# При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.
# Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:
#     оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки.
#     Результатом работы оператора должен являться новый экземпляр класса SortedList
#     оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки.
#     Результатом работы оператора должен являться левый экземпляр класса SortedList
# Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:
#     оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой.
#     Результатом работы оператора должен являться новый экземпляр класса SortedList
#     оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой.
#     Результатом работы оператора должен являться левый экземпляр класса SortedList
# Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.
# Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
# Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан.
# Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.
# Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
# Примечание 5. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной.
# Однако попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.

from collections.abc import Sequence

class SortedList(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = list(sorted(iterable))

    def add(self, obj):
        self.iterable.append(obj)
        self.iterable.sort()

    def discard(self, other):
        self.iterable = [i for i in  self.iterable if i != other]

    def update(self, obj):
        self.iterable.extend(obj)
        self.iterable.sort()

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.iterable[item]
        return NotImplemented

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        if isinstance(key, int):
            del self.iterable[key]
        return NotImplemented

    def __len__(self):
        return len(self.iterable)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.iterable += other.iterable
            self.iterable.sort()
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.iterable * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.iterable *= other
            self.iterable.sort()
            return self
        return NotImplemented

    def __str__(self):
        return f'SortedList({self.iterable})'

    def append(self, *args):
        raise NotImplementedError

    def insert(self, *args):
        raise NotImplementedError

    def extend(self, *args):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __contains__(self, item):
        return item in self.iterable

