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


from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push('x')