# Реализуйте контекстный менеджер reversed_print с помощью декоратора @contextmanager, который не принимает никаких аргументов.
# Контекстный менеджер reversed_print должен позволять выполнять все операции записи в стандартный поток вывода sys.stdout внутри блока with в обратном порядке.
# Примечание 1. Наглядные примеры использования класса reversed_print продемонстрированы в тестовых данных.
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

from contextlib import contextmanager
import sys

@contextmanager
def reversed_print():
    temp = sys.stdout.write
    sys.stdout.write = lambda x: temp(x[::-1])
    yield
    sys.stdout.write = temp
