# # С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных:
# Класс Animal должен иметь два метода экземпляра:
#     sleep() — пустой метод
#     eat()— пустой метод
# Класс Fish должен иметь один метод экземпляра:
#     swim()— пустой метод
# Класс Bird должен иметь один метод экземпляра:
#     lay_eggs()— пустой метод
# Класс FlyingBird должен иметь один метод экземпляра:
#     fly()— пустой метод

class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass
