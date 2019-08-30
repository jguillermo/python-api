def ejm(a=1, b=2):
    return a + b


class A:
    def ejemplo(self, **kwargs):
        return ejm(**kwargs)


obj = A()

print(obj.ejemplo())
print(obj.ejemplo(a=10))
print(obj.ejemplo(b=20))
print(obj.ejemplo(a=100, b=200))
