import funcs, os, sys

def say_hello():
    print('Hello World!')

print(__name__)
print(os.path.dirname(__file__))

say_hello()


def my_custom_function(a:int=1, b:int=2)->None:
    print(a+b)

my_custom_function()