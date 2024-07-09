# Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:
#     version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1.
#     Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
# Экземпляр класса Version должен иметь следующее формальное строковое представление:
# Version('<версия ПО в виде трех целых чисел, разделенных точками>')
# И следующее неформальное строковое представление:
# <версия ПО в виде трех целых чисел, разделенных точками>
# Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.
# Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше.
# Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают.
# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
# Примечание 2. Никаких ограничений касательно реализации класса Version нет, она может быть произвольной.

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version) -> None:
        mylist = [int(i) for i in version.split('.')]
        if len(mylist) == 3:
            self.versoin = mylist
        elif len(mylist) == 2:
            self.versoin = mylist + [0]
        elif len(mylist) == 1:
            self.versoin = mylist + [0] + [0]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{'.'.join(map(str, self.versoin))}')"

    def __str__(self) -> str:
        return f"{'.'.join(map(str, self.versoin))}"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Version):
            return self.versoin == value.versoin
        return NotImplemented

    def __lt__(self, value: object):
        if isinstance(value, Version):
            return self.versoin < value.versoin
        return NotImplemented
