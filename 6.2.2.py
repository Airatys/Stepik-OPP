# Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None.
# В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.
# Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:
#     default — значение по умолчанию для неопределенных элементов разреженного массива
# Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов.
# При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
# Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.

class SparseArray:
    def __init__(self, default):
        self.default = default

    def __getitem__(self, item):
        return self.__dict__.get(item, self.default)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
