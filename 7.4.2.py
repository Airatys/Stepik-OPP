# Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key).
# Процесс создания экземпляра класса EasyDict должен совпадать с процессом создания экземпляра класса dict.
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной.

class EasyDict(dict):
    def __init__(self, value):
        super().__init__(value)

    def __getattr__(self, item):
        return super().__getitem__(item)