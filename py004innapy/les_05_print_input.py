a = -6.84
print(1, a)

print(1, 2, 3, sep="-", end=" -> end")
print()

print("Hello", end=" ")
print("World")

b = "ads"

print("aaaa", end=b)
print()

x = 123
y = 321
print(f"x = {x} y = {y}")


# a = input("Input something: ")
# a = int(a)
# b = abs(a)
# print(a, type(a))

a = float("2.32")
print(a, type(a))

# a = float(input("a = "))
# b = float(input("b = "))
# c = 2 * (a + b)
# print(c, type(c))

a, b = map(float, input("a, b = ").split())
c = 2 * (a + b)
print(c, type(c))
