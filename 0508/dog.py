class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name

d = Dog("Fido")
e = Dog("Buggy")

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)