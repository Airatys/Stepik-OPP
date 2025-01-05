# Реализуйте класс JsonSerializableMixin, добавляющий классам функционал сериализации экземпляров класса в JSON-формат.
# Класс JsonSerializableMixin должен иметь один метод экземпляра:
#     to_json() — метод, возвращающий JSON-представление экземпляра класса
# JSON-представлением экземпляра класса должна быть строка формата json, полученная путем сериализации словаря атрибутов экземпляра класса.
# Примечание 1. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса JsonSerializableMixin нет, она может быть произвольной.

import json

class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)