my_list = [1, 2, 3]
print(my_list)

my_list.append(40)
print(my_list)

my_list.append(True)
print(my_list)

my_list.insert(2, 50)
print(my_list)

my_list.remove(True)
print(my_list)

print(my_list.pop())
print(my_list)

a = [1, 2, 3]
b = a.copy()
a[0]= "A"
print(a)
print(b)
