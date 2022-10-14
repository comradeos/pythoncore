


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