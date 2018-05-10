def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return "hello world"

    h = g


x = C()

print(x)
print(x.f(1,2))
print(x.g())
print(x.h())
print(x.h)
print(x.g)