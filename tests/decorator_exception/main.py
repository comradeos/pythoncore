def my_dec(func):
    def wrapper(*args, **kwargs):
        print("- start -")
        result = func(*args, **kwargs)
        print("- end -")
        return result
    return wrapper


@my_dec
def hello(a, b):
    print("hello")
    return a + b


a = hello(2, 5)
print(a)