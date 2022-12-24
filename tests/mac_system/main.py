import funcs, os, sys

def say_hello():
    print('Hello World!')

print(__name__)
print(os.path.dirname(__file__))

say_hello()
