# типы данных

# изменяемые
my_list = list([1, 2, 3])
my_dict = dict({'key': 'value'})
my_set = set({1, 2, 3, 4, 5})

# неизменяемые
my_int = int(1)
my_float = float(2.23)
my_str = str("hello")
my_bool = bool(True)
my_data = None
my_tuple = tuple(('a', 'b', 'c'))
my_frozenset = frozenset({1, 2, 3, 4, 5})

# == is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # сравнение по значению True
print(a is b)  # сравнение по адресу в пасяти False


# args, kwargs
def my_func(*args, **kwargs):
    print(args, kwargs)


my_func(1, 2, 3, hello='world')  # (1, 2, 3) {'hello': 'world'}

some_string = "hello"
print(some_string[0])
some_string = list(some_string)
some_string[0] = 'H'
some_string = ''.join(some_string)  # объединить элементы списка в строку
print(some_string)

a = 'A'
print(a.replace('A', 'B'))  # заменить в строке

my_list = [1, 2, 3]


def my_func(some_list: list) -> None:
    some_list[0] = 'A'


my_func(my_list)
print(my_list)

my_str = 'abc'


def my_func(some_str: str) -> None:
    some_str.replace('a', 'b')


my_func(my_str)
print(my_str)


# анотации типов
class A:
    prop_a: list
    prop_b: int

    @staticmethod  # статический метод
    def some_func(some_int: int) -> None:
        print(some_int)


a = A()
A.some_func(231)

# лямбда функция

my_list = [1, 2, 3]
print(my_list)
my_list = map(lambda x: x + 10, my_list)
my_list = list(my_list)
print(my_list)

my_list = filter(lambda x: x > 12, my_list)
print(list(my_list))

# тернарный оператор
a = 10
b = 'a' if a == 10 else 'b'
print(b)

# глубокая и поверхностная копии
import copy

a = [1, 2, 3]
b = copy.copy(a)  # поверхностная
b[0] = 777
print(a)
print(b)

a = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]
b = copy.deepcopy(a)  # глубокая
b[0][0] = 777
print(a)
print(b)


# виртуальная среда venv
# python -m venv my_env


class A:
    public_var: str
    _protected_var: int = 231
    __private_var: float

    def __init__(self, public_var: str = 'a', protected_var: int = 1, private_var: float = 1.0, ):
        self.public_var = public_var
        self._protected_var = protected_var
        self.__private_var = private_var

    @classmethod
    def my_class_method(cls):
        print('classmethod')

    @staticmethod
    def my_static_method():
        print('staticmethod')


A.my_static_method()
a = A()
print(a._A__private_var)

print('-' * 100)


# декораторы


def my_decorator(some_func):
    def wrapper(*args, **kwargs):
        print('A..')
        some_func()
        print('..B')
        print(args, kwargs)

    return wrapper


@my_decorator
def my_func():
    print('my_func')


my_func(1, 2, 3, hello='world')


# res = my_decorator(my_func)
# res(1, 2, 3, a='b') # без использования синт. сахара


# декоратор с пробросом аргументов
def my_decorator_args(arg=1):
    def decorator(some_func):
        def wrapper(*args, **kwargs):
            print('A..')
            some_func()
            print('..B')
            print(args, kwargs)
            print(arg)

        return wrapper

    return decorator


# @my_decorator_args(777)
def my_func_arg():
    print('my_func')


# my_func_arg(1, 2, 3, hello='world')

# dec = my_decorator_args(123)
# b = dec(my_func_arg)
# b()


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass


print(A.__mro__)  # Method Resolution Order


# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

class A: pass


A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
a = A()
print(a.MAX_COORD)


class A1: pass


class B1: pass


class C1(A1, B1): pass


print(C1.__mro__)
