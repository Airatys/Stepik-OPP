# Реализуйте класс Seasons, описывающий перечисление с временами года. Перечисление должно иметь четыре элемента:
#     WINTER — элемент со значением 1
#     SPRING — элемент со значением 2
#     SUMMER — элемент со значением 3
#     FALL — элемент со значением 4
# Элемент перечисления должен иметь один метод:
#     text_value() — метод, принимающий в качестве аргумента код страны en или ru и возвращающий строковое значение элемента в зависимости от переданного аргумента.
#     Для WINTER en и ru значениями являются winter и зима соответственно, для SPRING — spring и весна, для SUMMER — summer и лето, для FALL — fall и осень
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса Seasons нет, она может быть произвольной.

from enum import Enum

class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, item):
        if item == 'en':
            return self.name.lower()
        else:
            return ['зима', 'весна', 'лето', 'осень'][self.value - 1]