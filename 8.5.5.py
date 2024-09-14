# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы.
# Например, bee_geek и hello_world.
# Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
# Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого. Например, beeGeek и helloWorld.
# Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:
#     attrs — булево значение, по умолчанию равняется False
# Декоратор должен переименовывать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и lower Camel Case на Snake Case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса.
# Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel Case на Snake case, если False — остаться прежним.
# Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, lower Camel Case или Snake Case.

import re

def snake_case(attrs=False):
    def decorator(cls):
        mydict = {k:v for k, v in cls.__dict__.items()}
        for key in mydict.keys():
            if not '__' == key[0:2]:
                value = getattr(cls, key)
                if callable(value):
                    regex = re.sub(r'_?\B([A-Z])', r'_\1', key).lower()
                    setattr(cls, regex, value)
                    delattr(cls, key)

                elif not callable(value) and attrs:
                    regex = re.sub(r'\B([A-Z])\B', r'_\1', key).lower()
                    setattr(cls, regex, value)
                    delattr(cls, key)
        return cls
    return decorator

