# Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
#     string — значение строки
# Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
# <значение строки
# Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.
# Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
#     результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n
#     результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
#     результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов.
#     Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
#     результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов.
#     Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
# Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.
# Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.
# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
# Примечание 3. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.

class SuperString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__class__(self.string[:len(self.string) // other])
        return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __lshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.__class__(self.string)
            if len(self.string) <= other:
                return self.__class__('')
            else:
                return self.__class__(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.__class__(self.string)
            if len(self.string) <= other:
                return self.__class__('')
            else:
                return self.__class__(self.string[other:])
        return NotImplemented
