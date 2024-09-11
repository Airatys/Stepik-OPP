# 1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:
#     MONDAY — элемент со значением 0
#     TUESDAY — элемент со значением 1
#     WEDNESDAY — элемент со значением 2
#     THURSDAY — элемент со значением 3
#     FRIDAY — элемент со значением 4
#     SATURDAY — элемент со значением 5
#     SUNDAY — элемент со значением 6
# 2. Также реализуйте класс NextDate, который позволяет определять следующую ближайшую дату, соответствующую указанному дню недели: например, дату ближайшего вторника или дату ближайшей пятницы.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#     today — текущая дата, представленная экземпляром класса date. Относительно этой даты должна определяться следующая ближайшая дата, соответствующая некоторому дню недели
#     weekday — день недели, представленный элементом перечисления Weekday
#     considering_today — булево значение, по умолчанию равняется False
#
# Параметр considering_today должен определять, учитывается ли дата today при определении даты, соответствующей дню недели weekday.
# Если параметр имеет значение True, дата today должна учитываться, если False — не учитываться.
# Например, если день недели даты today равен weekday и параметр considering_today равен True, то искомой датой, соответствующей дню недели weekday, будет являться сама дата today.
# Класс NextDate должен иметь два метода экземпляра:
#     date() — метод, возвращающий следующую ближайшую (относительно даты today) дату, соответствующую дню недели weekday, в виде экземпляра класса date
#     days_until() — метод, возвращающий количество дней до следующей ближайшей (относительно даты today) даты, соответствующей дню недели weekday
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

from enum import Enum, IntEnum
from datetime import timedelta

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday, considering_today=False):
        self.today = today
        self.weekday = weekday.value
        self.considering_today = considering_today
        self.day = (self.weekday - self.today.weekday()) % 7

    def date(self):
        if self.today.weekday() == self.weekday and self.considering_today:
            return self.today
        else:
            self.day = self.day if self.day != 0 else 7
        return self.today + timedelta(days=self.day)

    def days_until(self):
        return self.day

