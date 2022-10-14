class C1:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


c1 = C1(1, 2, 3, a=1, b=2, c=3)
print(c1.args, c1.kwargs)

a = set([1, 2, 3, 3, 3, 3, 3])
a.add(9)
print(a)
b = frozenset([1, 2, 3, 3, 3, 3, 3])
print(b)

from typing import List, TypeVar, Any


def first(container: List[Any]) -> Any:
    return container[0]


list_one: List[str] = ["a", "b", "c"]
print(first(list_one))

list_two: List[int] = [1, 2, 3]
print(first(list_two))
