# Будем называть словом любую последовательность из одной или более латинских букв.
# 1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен принимать один аргумент:
#     length — длина строки абзаца
# Класс LeftParagraph должен иметь два метода экземпляра:
#     add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац.
#     Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
#     end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
# 2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс должен принимать один аргумент:
#     length — длина строки абзаца
# Класс RightParagraph должен иметь два метода экземпляра:
#     add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац.
#     Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
#     end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.


# ЛЕНЬ БЫЛО РЕШАТЬ ВЕРНУСЬ ПОЗЖЕ)))
#
#
#
# from abc import ABC, abstractmethod
#
# class LeftParagraph(ABC):
#     def __init__(self, length):
#         self.length = length
#         self.text = ''
#
#     def add(self, string):
#         if
#         self.text += string
#
#     @abstractmethod
#     def end(self):
#         string = 'Hello'
#         space = ' '
#         side = '<'
#         print(f'{string:{space}{side}{self.length}}')
#
#
# class RightParagraph(LeftParagraph):
#     def end(self):
#         pass
#
# leftparagraph = LeftParagraph(10)
#
# leftparagraph.add('death')
# leftparagraph.add('can have me')
# leftparagraph.add('when it earns me')
# leftparagraph.end()
