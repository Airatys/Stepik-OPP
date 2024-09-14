# Реализуйте декоратор @singleton для декорирования класса.
# Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.

import functools

def singleton(cls):
    obj_cls = cls.__new__
    @functools.wraps(obj_cls)
    def new_cls(self, *args, **kwargs):
        if not hasattr(cls, 'sing'):
            cls.sing = obj_cls(cls)
        return cls.sing
    cls.__new__ = new_cls
    return cls