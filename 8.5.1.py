# Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.
# Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в котором они были созданы.

import functools

def track_instances(cls):
    obj_init = cls.__init__
    cls.instances = []

    @functools.wraps(obj_init)
    def new_init(self, *args, **kwargs):
        obj_init(self, *args, **kwargs)
        cls.instances.append(self)
    cls.__init__ = new_init
    return cls


