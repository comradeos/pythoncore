import funcs, os, sys

def say_hello():
    print('Hello World!')

print(__name__)
print(os.path.dirname(__file__))

say_hello()




def contribute_something(value_1=1, value_2=1)->int:
    return value_1+value_2

print(contribute_something("sds",2))