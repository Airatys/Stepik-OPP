# Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
# код страны 	формат даты
# ru 	DD.MM.YYYY
# us 	MM-DD-YYYY
# ca 	YYYY-MM-DD
# br 	DD/MM/YYYY
# fr 	DD.MM.YYYY
# pt 	DD-MM-YYYY
# Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты в формат определенной страны из таблицы выше.
# При создании экземпляра класс должен принимать один аргумент:
#     country_code — код страны
# Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:
#     d — дата (тип date)
# Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 2. Никаких ограничений касательно реализации класса DateFormatter нет, она может быть произвольной.

from datetime import  date

class DateFormatter:
    _country_code = {'ru': '%d.%m.%Y',
                    'us': '%m-%d-%Y',
                    'ca': '%Y-%m-%d',
                    'br': '%d/%m/%Y',
                    'fr': '%d.%m.%Y',
                    'pt': '%d-%m-%Y', }
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        return date.strftime(d, self._country_code[self.country_code])