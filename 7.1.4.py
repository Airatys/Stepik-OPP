# Реализуйте класс User, описывающий пользователя некоторого интернет-ресурса. При создании экземпляра класс должен принимать один аргумент:
#     name — имя пользователя
# Класс User должен иметь один метод экземпляра:
#     skip_ads() — метод, всегда возвращающий False
# Также реализуйте класс PremiumUser, наследника класса User, описывающий пользователя некоторого интернет-ресурса с премиум подпиской.
# Процесс создания экземпляра класса PremiumUser должен совпадать с процессом создания экземпляра класса User.
# Класс PremiumUser должен иметь один метод экземпляра:
#     skip_ads() — метод, всегда возвращающий True
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

class User:
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False

class PremiumUser(User):
    def __init__(self, name):
        User.__init__(self, name)

    def skip_ads(self):
        return True


