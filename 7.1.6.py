# 1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен принимать один аргумент:
#     start — начальное значение счетчика, по умолчанию равняется 0
# Экземпляр класса Counter должен иметь один атрибут:
#     value — текущее значение счетчика
# Класс Counter должен иметь два метода экземпляра:
#     inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.
#     Если число не передано, метод должен увеличить значение счетчика на единицу
#     dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число.
#     Если число не передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным
# 2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать, но нельзя уменьшать.
# Процесс создания экземпляра класса NonDecCounter должен совпадать с процессом создания экземпляра класса Counter.
# Экземпляр класса NonDecCounter должен иметь один атрибут:
#     value — текущее значение счетчика
# Класс NonDecCounter должен иметь один метод экземпляра:
#     dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counter
# 3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать лишь до определенного числа.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     start — начальное значение счетчика, по умолчанию равняется 0
#     limit — максимально возможное значение счетчика, по умолчанию равняется 10
# Экземпляр класса LimitedCounter должен иметь один атрибут:
#     value — текущее значение счетчика
# Класс LimitedCounter должен иметь один метод экземпляра:
#     inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.
#     Если число не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения счетчика метод не должен превышать установленный лимит
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value -= n
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, n=1):
        if self.value + n < self.limit:
            self.value += n
        else:
            self.value = self.limit