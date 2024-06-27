# Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
# Экземпляр класса Todo должен иметь один атрибут:
#     things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:
#     add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
#     (<название дела>, <приоритет>)
#     get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
#     get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет 
#     get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет 
# Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(), должны располагаться в том порядке, в котором они были добавлены в список.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class Todo:
    def __init__(self):
        self.things = []
  
    def add(self, delo, priorit):
        self.things.append((delo, priorit))
        
    def get_by_priority(self, n):
        return [i[0] for i in self.things if i[1] == n]
    
    def get_low_priority(self):
        min_priorit = min(self.things, default='', key=lambda x: x[1])
        return [i[0] for i in self.things if i[1] == min_priorit[1]]
    
    def get_high_priority(self):
        max_priorit = max(self.things, default='', key=lambda x: x[1])
        return [i[0] for i in self.things if i[1] == max_priorit[1]]