class C1:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


c1 = C1(1, 2, 3, a=1, b=2, c=3)
print(c1.args, c1.kwargs)

a = {1, 2, 3, 3, 3, 3, 3}
a.add(9)
print(a)
b = frozenset([1, 2, 3, 3, 3, 3, 3])
print(b)

from typing import TypeVar, Generic, List

T = TypeVar('T')
print(T)


class MyClass:
    def __init__(self, name='unknown'):
        self.name = name

    def print_name(self):
        print(self.name)


obj1 = MyClass('Iaroslav')
obj1.print_name()
