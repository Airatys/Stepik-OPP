# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Gun должен иметь три метода экземпляра:
#     shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
#     shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
#     shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля


class Gun:
    def __init__(self):
        self.shots = 0
        self.count = 0

    def shoot(self):
        self.shots += 1
        if self.count == 0:
            self.count += 1
            print('pif')
        else:
            self.count -= 1
            print('paf')

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0
        self.count = 0

