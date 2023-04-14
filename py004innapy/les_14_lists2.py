a = [1, 2, 3, 4, 5, 6, 7]
print(a[2:5])
print(a[1:3])

b = a[:]
print(id(a))
print(id(b))

c = b

print("-" * 10)
print(id(b))
print(id(c))
