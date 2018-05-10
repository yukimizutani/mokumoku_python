class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = "1"

    def f(self):
        return 'hello world ' + self.data


x = MyClass()

# print(x.i)
# print(x.f)
# print(MyClass.f)
# print(MyClass.f(x))
# print(x.f())
# print(x.__doc__)
# print(x.data)

xf = x.f
print("******")
print(xf())
