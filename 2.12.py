# Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:
#     iterable — итерируемый объект
#     delimiter — значение-разделитель
# Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.
# Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3, а в качестве значения-разделителя — 0.
# Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми располагается число 0:
# 1 0 2 0 3
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию intersperse(), но не код, вызывающий ее.

def intersperse(iterable, delimiter):
    flag = True
    for i in iterable:
        if not flag:
            yield delimiter
        flag = False
        yield i

#через enumerate 

def intersperse(iterable, delimiter):
    for i, item in enumerate(iterable):
        if i:
            yield delimiter
        yield item

