# Реализуйте класс Atomic. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     data — произвольный список, множество или словарь
#     deep — булево значение, по умолчанию равняется False
# Экземпляр класса Atomic должен являться контекстным менеджером, который позволяет выполнять операции над коллекцией data внутри блока with в атомарном режиме, то есть либо все операции должны быть выполнены, либо ни одна из них.
# Если все операции корректны (не приводят к возбуждению исключения), они должны быть применены к коллекции data.
# Если какая-либо операция некорректна, все ранее выполненные операции должны быть отменены, а коллекция data должна быть возвращена в исходное состояние.
# Параметр deep должен определять состояние вложенных структур коллекции data после завершения блока with.
# Если он имеет значение False, контекстный менеджер должен возвращать в исходное состояние только саму коллекцию data, не затрагивая ее вложенные структуры.
# Например, если data является двумерным списком и внутри блока with произошло изменение одного из его вложенных списков, то этот вложенный список должен сохранить свое новое состояние, даже если последующие операции внутри блока with приведут к возбуждению исключения и возврату коллекции data в исходное состояние.
# Если же параметр deep имеет значение True, контекстный менеджер должен возвращать в исходное состояние не только саму коллекцию data, но и ее вложенные структуры.
# Примечание 1. Наглядные примеры использования класса Atomic продемонстрированы в тестовых данных.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Класс Atomic должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

import copy

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.data_copy = copy.deepcopy(self.data) if self.deep else copy.copy(self.data)

    def __enter__(self):
        return self.data_copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            return True
        if isinstance(self.data, list):
            self.data[:] = self.data_copy
        if isinstance(self.data, set|dict):
            self.data.clear()
            self.data.update(self.data_copy)
        return False


