# Реализуйте класс Money, описывающий денежную сумму в рублях. При создании экземпляра класс должен принимать один аргумент:
#     amount — количество денег
# Экземпляр класса Money должен иметь следующее неформальное строковое представление:
# <количество денег> руб.
# Также экземпляр класса Money должен поддерживать унарные операторы + и -:
#     результатом унарного + должен являться новый экземпляр класса Money с неотрицательным количеством денег
#     результатом унарного - должен являться новый экземпляр класса Money с отрицательным количеством денег
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса Money нет, она может быть произвольной.

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} руб."

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        if self.amount < 0:
            return Money(self.amount)
        return Money(-self.amount)