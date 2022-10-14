


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





nums = [1, 2, 3, 4]
print(list(map(lambda x: x + 10, nums))) # преобразовать в список(пройтись по списку nums и применить к каждому элементу функцию lambda x: x + 10)

print(list(filter(lambda x: x > 2, nums))) # [3, 4]
print(list(map(lambda x: x + 100, nums))) # [101, 102, 103, 104]





a = 5
b = 10 if a < 10 else 20
print(b) # 10 

a = 15
b = 10 if a < 10 else 20
print(b) # 20







from copy import copy, deepcopy
from tkinter.tix import TList
some = [1, [2] ,3]
 
print(some[1] is copy(some)[1]) # True
print(some[1] is deepcopy(some)[1]) # False


a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(a)

b = deepcopy(a)
b[0][0] = 777
print(b)
print(a)


print(1 in [1,2,3])


# хэш

print(hash("hello"))
print('\n\n\n')







def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
    print(arr)
    
    
    
    
def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(arr)
            
    
arr = [64, 34, 25, 12, 22, 11, 11, 90]
 
# bubbleSort(arr)
bubble(arr)


# Операции списка и их временная сложность
# Вставка: O(n).
# Получение элемента: O(1).
# Удаление элемента: O(n).
# Проход: O(n).
# Получение длины: O(1).



# Операции с множествами и их временная сложность
# Проверить наличие элемента в множестве: O(1).
# Отличие множества A от B: O(длина A).
# Пересечение множеств A и B: O(минимальная длина A или B).
# Объединение множеств A и B: O(N) , где N это длина (A) + длина (B).



# Операции со словарями и их временная сложность
# Здесь мы считаем, что ключ используется для получения, установки или удаления элемента.
# Получение элемента: O(1).
# Установка элемента: O(1).
# Удаление элемента: O(1).
# Проход по словарю: O(n).



class Person:
  about = 'This class stores the name and age for a person'
 
  def __init__(self, name, age):
        self.name = name
        self.age = age
 
  def details(self):
        print(f"Person's name is {self.name} and age is {self.age}")
 
  @classmethod
  def info(aaa):
    print(aaa.about)
 
 
Person.info()





class A:
    num:int
    word:str
    
    def __init__(self, num_arg:int, word_arg:str)->None:
        self.num = num_arg
        self.word = word_arg
        
    def show_num(self)->None:
        print(self.num)    
    
    def show_word(self)->None:
        print(self.word)


class B(A):
    dec:float
    
    def __init__(self, num_arg:int, word_arg:str, dec_arg:float)->None:
        super().__init__(num_arg, word_arg)
        self.dec = dec_arg
    
    def show_dec(self)->None:
        print(self.dec)



obj = B(123, 'hello', 2.552)
obj.show_num()
obj.show_word()
obj.show_dec()

obj = A(222, 'world')
obj.show_num()
obj.show_word()




print('-'*50)





class A3:
    some_value = 0 # public
    _some_value = 0 # protected (виден из класса и классов его наследующих)
    __some_value = 0 # private
    
    def a(self): # метод объекта 
        pass
    
    @classmethod
    def b(cls): # метод класса
        print(cls.num)
        pass
    
    @staticmethod
    def c(): 
        print(31313)
        pass
    
   
class B3(A3):
    pass

a = A3()
# print(a.__some_value) # a._A3__some_value




print('-'*50)


# декоратор

def dec_func(func):
    def wrapper():
        print(1)
        print(2)
        func()
        print(3)
        
    return wrapper

@dec_func
def f1():
    print('hello from f1()')

f1()



# декоратор с аргументами

def my_dec_args(func):
    def wrapper(*args, **kwargs):
        print(12)
        func()
        print(args)
        print(kwargs)
        
    return wrapper
    

@my_dec_args
def f2():
    print('hello form f2()')
    
f2(31,23,12,3, aaaa=2312)






print('-'*50)
# без синтаксического сахара
def decorator(f):
    def wrp(*args, **kwargs):
        print(1)
        f()
        print(2)
        print(args)
        print(kwargs)
    return wrp

def f1():
    print('f1')

dec_func_1 = decorator(f1)
dec_func_1(1,2,3)





# АБСТРАКТНЫЙ КЛАСС И МЕТОДЫ
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def some():pass

class B(A):
    def some():pass

a = B()


# МЕТА КЛАСС
from abc import ABCMeta
class OneMeta(ABCMeta):
    pass
class TwoMeta(type):
    pass






class AbstractOne(ABC):
    @abstractmethod
    def show(self):
        pass
    
    
class MyClassA(AbstractOne):
    __private = 777
    def __init__(self, a, b): 
        self.a = a
        self.b = b
        pass
    def show(self): 
        print(self.a, self.b)
        
obj1 = MyClassA(111,222)
obj1.show()
print(obj1._MyClassA__private)

class MyClassB(MyClassA):
    def __init__(self, a, b):
        super().__init__(a, b)


b = MyClassB(3,5)
# print(b._MyClassB__private) # ошибка



class Shark():
    def swim(self):
        print("The shark is swimming.")
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")
        
class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")
    def swim_backwards(self):
        print("The clownfish can swim backwards.")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")





class Mix1:
    def text1(self):
        print('Mix1')

class Mix2:
    def text(self):
        print('Mix2')
class Base:
    def text(self):
        print('Base')
        
class MyClass(Base, Mix1, Mix2):
    pass

obj = MyClass()
obj.text1()