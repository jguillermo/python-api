
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    aaa=None
    def __init__(self) :
        print('*********ENTRO AL CONTRUCTOR*********')
        print(self.aaa)
        self.aaa=1
        print(self.aaa)



obj = MyClass()
print(obj.aaa)
obj.aaa=2
print(obj.aaa)

obj2 = MyClass()
print('objeto 2')
print(obj2.aaa)
obj2.aaa=3
print(obj.aaa)
