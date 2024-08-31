# Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр.
# Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.
# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
# Примечание 2. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.

class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() != other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() > other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (self.__class__, str)):
            return self.lower() >= other.lower()
        return NotImplemented

    def __contains__(self, other):
        return other.lower() in self.lower()
