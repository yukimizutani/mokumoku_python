class BaseClassName:
    def parent_method(self):
        print("parent")


class DerivedClassName(BaseClassName):
    def child_method(self):
        BaseClassName.parent_method(self)
        print("child")


c = DerivedClassName()

c.parent_method()
c.child_method()

print(isinstance(c, DerivedClassName))
print(isinstance(c, int))
print(isinstance(c, BaseClassName))
print(issubclass(DerivedClassName, BaseClassName))
print(issubclass(BaseClassName, DerivedClassName))
print(issubclass(BaseClassName, object))