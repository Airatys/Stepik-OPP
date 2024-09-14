# Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:
#     filename — имя json файла, содержимым которого является JSON объект
# Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.

import json

def jsonattr(obj):
    def decorator(cls):
        with open(obj, encoding='u8') as file_js:
            json_file = json.load(file_js)
            for k, v in json_file.items():
                setattr(cls, k, v)
            return cls
    return decorator
