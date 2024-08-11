# Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:
#     data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
# Класс HistoryDict должен иметь пять методов экземпляра:
#     keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
#     values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
#     items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
#     history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу.
#     Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
#     all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
# При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.
# Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.
# Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся.
# Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.
# Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.
# Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class HistoryDict:
    def __init__(self, data={}):
        self.__dict__ = {k: [v] for k, v in data.items()}

    def keys(self):
        return self.__dict__

    def values(self):
        yield from (value[-1] for value in self.__dict__.values())

    def items(self):
        yield from ((key, value[-1]) for key, value in self.__dict__.items())

    def history(self, key):
        return self.__dict__.get(key, [])

    def all_history(self):
        return self.__dict__

    def __getitem__(self, item):
        return self.__dict__.get(item)[-1]

    def __setitem__(self, key, value):
        self.__dict__.setdefault(key, []).append(value)

    def __delitem__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        yield from self.__dict__