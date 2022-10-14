some_string = "12345"
# some_string[3] = "9" # ошибка
# some_string = some_string.replace('3','9')
print(some_string)




def some_func(some_arg: list = []) -> list: # передача осуществляется  по ссылкам в памяти
    some_arg.append(1)
    return some_arg

print(some_func()) # [1]
print(some_func()) # [1,1]
print(some_func()) # [1,1,1]
print(some_func()) # [1,1,1,1]




def some_func_2(some_arg: str = "") -> str: # передача осуществляется  по значению
    return some_arg

print(some_func_2()) # 1
print(some_func_2()) # 1
print(some_func_2()) # 1
print(some_func_2()) # 1


def some_func_3(*args, **kwargs) -> None: # передача осуществляется  по значению
    print(args[0])
    print(args)
    print(kwargs['a'])
    print(kwargs)

some_func_3(421,221, a = 777, b = 45) # (12, 41232) {'a': 12, 'b': 234}







# lambda
some_list = [1,'s',2,'a',3, 'a']

def check(item):
    return isinstance(item, str)

some_list_filtered = filter(check, some_list) # list(filter(check, some_list))

for i in some_list_filtered:
    print(i)
    
my_lambda = lambda x: x + 10

print(my_lambda(12))