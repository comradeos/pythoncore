import ctypes
import os

os.chdir(os.path.dirname(__file__))

lib = ctypes.CDLL('./ext_lib')

lib.HelloWorld()

a = lib.Sum(2,3)

print(a)