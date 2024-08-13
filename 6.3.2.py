# Реализуйте функцию non_closed_files(), которая принимает один аргумент:
#     files — список файловых объектов
# Функция должна возвращать список, элементами которого являются открытые файловые объекты из списка files.
# Примечание 1. Файловые объекты в возвращаемом функцией списке должны располагаться в своем исходном порядке.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию non_closed_files(), но не код, вызывающий ее.

def non_closed_files(files):
    for i in files:
        if not i.closed:
            yield i
