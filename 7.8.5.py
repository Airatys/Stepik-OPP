# 1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#     topic — тема выступления
#     start_time — время начала выступления в виде строки в формате HH:MM
#     duration — длительность выступления в виде строки в формате HH:MM
# 2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день.
# Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Conference должен иметь четыре метода экземпляра:
#     add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию.
#     Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
#     Провести выступление в это время невозможно
#     total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
#     longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
#     longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строки в формате HH:MM
# Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
# Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = self.time_to_num(start_time)
        self.duration = self.time_to_num(duration)
        self.end_time = self.start_time + self.duration
        self.period = range(self.start_time, self.end_time)

    def time_to_num(self, s: str) -> int:
        h, m = map(int, s.split(':'))
        return h * 60 + m

class Conference:
    def __init__(self):
        self.timetable = []

    def add(self, lecture):
        for exist in self.timetable:
            if set(exist.period) & set(lecture.period):
                raise ValueError('Провести выступление в это время невозможно')
        self.timetable.append(lecture)
        self.timetable.sort(key=lambda lecture: lecture.start_time)

    def total(self):
        amount = sum(lecture.duration for lecture in self.timetable)
        return f'{amount // 60:02d}:{amount % 60:02d}'

    def longest_lecture(self):
        sabj = max(lecture.duration for lecture in self.timetable)
        return f'{sabj // 60:02d}:{sabj % 60:02d}'

    def longest_break(self):
        max_break = 0
        for i in range(len(self.timetable) - 1):
            max_break = max(self.timetable[i + 1].start_time - self.timetable[i].end_time, max_break)
        return f'{max_break // 60:02d}:{max_break % 60:02d}'