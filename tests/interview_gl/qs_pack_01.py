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

my_list = [1, 2, 3]
print(my_list)
my_list = map(lambda x: x + 10, my_list)
my_list = list(my_list)
print(my_list)


my_list = filter(lambda x: x > 12, my_list)
print(list(my_list))

