# Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами.
# При создании экземпляра класс не должен принимать никаких аргументов.
# Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:
#     a — число
#     b — число
#     operation — один из символов +, -, * и /
# Если operation равняется +, экземпляр класса Calculator должен вернуть сумму a и b, если - — разность a и b, если * — произведение a и b, если / — частное a и b.
# При попытке выполнить деление на ноль должно быть возбуждено исключение ValueError с текстом:
# Деление на ноль невозможно
# Примечание 1. Числами будем считать экземпляры классов int и float.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 3. Никаких ограничений касательно реализации класса Calculator нет, она может быть произвольной.

class Calculator:
    def __call__(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                raise ValueError('Деление на ноль невозможно')
            return a / b