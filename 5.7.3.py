# Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен принимать один аргумент:
#     number — число в римской системе счисления. Например, IV
# Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:
# <число в римской системе счисления>
# Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.
# Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.
# Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:
#     результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
#     результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
# Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.
# Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.
# Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.
# Примечание 4. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.

from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def roman_to_int(s):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and val[s[i]] > val[s[i - 1]]:
                result += val[s[i]] - 2 * val[s[i - 1]]
            else:
                result += val[s[i]]
        return result

    @staticmethod
    def int_to_roman(s):
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                         'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman = ''
        for letter, value in roman_numbers.items():
            while s >= value:
                roman += letter
                s -= value
        return roman

    def __str__(self):
        return f"{self.number}"

    def __int__(self):
        return self.roman_to_int(self.number)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.roman_to_int(self.number) == other.roman_to_int(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.roman_to_int(self.number) < other.roman_to_int(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.int_to_roman(self.roman_to_int(self.number) + other.roman_to_int(other.number)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.int_to_roman(self.roman_to_int(self.number) - other.roman_to_int(other.number)))
        return  NotImplemented