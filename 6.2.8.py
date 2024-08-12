# Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:
#     string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
# Класс MutableString должен иметь два метода экземпляра:
#     lower() — метод, переводящий все символы изменяемой строки в нижний регистр
#     upper() — метод, переводящий все символы изменяемой строки в верхний регистр
# Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:
# <текущее значение изменяемой строки>
# Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:
# MutableString('<текущее значение изменяемой строки>')
# При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.
# Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.
# Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
# Экземпляр класса MutableString должен поддерживать полноценные срезы, результатами которых должны быть новые изменяемые строки.
# Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.
# Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных атрибутов нет.
# Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class MutableString:
    def __init__(self, string=''):
        self._string = string

    def _set_or_del(self, key, value=None):
        tmp = list(self._string)
        if value:
            tmp[key] = value
        else:
            del tmp[key]
        return tmp

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __str__(self):
        return self._string

    def __repr__(self):
        return f"MutableString('{self._string}')"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        return iter(self._string)

    def __delitem__(self, key):
        tmp = self._set_or_del(key)
        self._string = ''.join(tmp)

    def __setitem__(self, key, value):
        tmp = self._set_or_del(key, value)
        self._string = ''.join(tmp)

    def __getitem__(self, key):
        return MutableString(self._string[key])

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self._string + other._string)
        return NotImplemented
