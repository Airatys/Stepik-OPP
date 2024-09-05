# Вам доступны классы Average, Median и Harmonic, имеющие сходный интерфейс.
# Все три класса используются для обработки пользовательских оценок и оценок критиков некоторого медиаконтента по стобалльной шкале и вычисления средних значений этих оценок.
# Задачей класса Average является нахождение среднего арифметического пользовательских оценок или оценок критиков, классов Median и Harmonic — медианы и среднего гармонического соответственно.
# Изучите приведенные классы, реализуйте абстрактный базовый класс Middle и постройте корректную схему наследования. При выполнении старайтесь избегать дублирования кода.
# Примечание 1. Функционал классов Average, Median и Harmonic должен остаться прежним, необходимо лишь объединить их в иерархию, определив для них единый базовый абстрактный класс Middle.

from abc import ABC, abstractmethod

class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes

    def get_correct_user_votes(self):
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    @abstractmethod
    def get_average(self, users=True):
        pass

class Average(Middle):
    def get_average(self, users=True):
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()
        return sum(votes) / len(votes)


class Median(Middle):
    def get_average(self, users=True):
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())
        return votes[len(votes) // 2]


class Harmonic(Middle):
    def get_average(self, users=True):
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))