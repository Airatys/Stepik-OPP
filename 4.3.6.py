# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Gun должен иметь один метод экземпляра:
#     shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее

class Gun:
    def __init__(self) -> None:
        self.count = 0
    
    def shoot(self):
        if self.count == 0:
            self.count += 1
            print('pif')
        else:
            self.count -= 1
            print('paf')
