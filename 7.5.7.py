# ДНК состоит из двух цепей, ориентированных азотистыми основаниями друг к другу.
# В ДНК встречается четыре вида азотистых оснований: аденин (A), гуанин (G), тимин (T) и цитозин (C).
# Азотистые основания одной из цепей соединены с азотистыми основаниями другой цепи водородными связями согласно принципу комплементарности: аденин (A) соединяется только с тимином (T), гуанин (G) — только с цитозином (C).
# Реализуйте класс DNA, описывающий двухцепочную спираль ДНК. При создании экземпляра класс должен принимать один аргумент:
#     chain — первая цепь ДНК, представляющая собой строку из символов A, G, T и C (азотистых оснований)
# Экземпляр класса DNA должен иметь следующее неформальное строковое представление:
# <азотистые основания первой цепи ДНК>
# При передаче экземпляра класса DNA в функцию len() должно возвращаться количество азотистых оснований в одной из его цепей.
# При передаче экземпляра класса в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса DNA, расположенные в обратном порядке.
# Помимо этого, экземпляр класса DNA должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
# Также экземпляр класса DNA должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
# В случае с функцией reversed(), итерацией и доступу по индексам элементы экземпляра класса DNA должны быть представлены в виде кортежей из двух элементов, первым из которых является основание первой цепи ДНК по указанному индексу, вторым — азотистое основание второй цепи ДНК по указанному индексу.
# Азотистое основание второй цепи ДНК можно получить при помощи принципа комплементарности.
# Вдобавок ко всему, экземпляр класса DNA должен поддерживать операцию проверки на принадлежность с помощью оператора in. В данном случае должно проверяться, входит ли азотистое основание в первую цепь ДНК.
# Экземпляры класса DNA должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две ДНК считаются равными, если их первые цепи совпадают.
# Наконец, экземпляры класса DNA должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса DNA, первой цепью которого является конкатенация первых цепей исходных экземпляров класса DNA.
# Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
# Примечание 2. Если объект, с которым выполняется операция сравнения или сложения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
# Примечание 3. Никаких ограничений касательно реализации класса DNA нет, она может быть произвольной.

from collections.abc import Sequence

class DNA(Sequence):
    def __init__(self, chain):
        self.chain = chain
        self.data = {'A': ('A', 'T'), 'T': ('T', 'A'), 'G': ('G', 'C'), 'C': ('C', 'G')}

    def __str__(self):
        return f'{self.chain}'

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.chain[key])
        else:
            return self.data.get(self.chain[key])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.chain == other.chain
        return NotImplemented

    def __contains__(self, item):
        return item in self.chain

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.chain + other.chain)
        return NotImplemented

