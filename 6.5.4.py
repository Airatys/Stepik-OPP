# Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:
#     filename — имя текстового файла
# Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце.
# Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.
# Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.obj = open(self.filename, encoding='u8')
        file = map(str.strip, self.obj)
        return file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.close()