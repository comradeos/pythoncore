s = "python"
print(s.upper())
print(s.lower())
print(s.capitalize())

s = "abracadabra"
print(s.count("ra"))
print(s.count("ra", 4))
print(s.count("ra", 4, 5))

print(s.find("br"))
print(s.find("br", 2))

print(s.rfind("br", 2))

# print(s.index("brf", 2))

s = "abcd abcd abcd"
print(s.replace("a", "@"))
print(s.replace("a", "@", 2))

s = "abc"
print(s.isalpha())

s = "abc23"
print(s.isalpha())

s = "123"
print(s.isdigit())

print("abc".rjust(5, "-"))

print("12".rjust(4, "0"))
print("12".ljust(4, "0"))

print("Ivanov Ivan Ivanovich".split(sep=" "))

digs = "1 , 2,, 3,    4, 5,,7,8,   9"
digs = digs.replace(" ", "")
print(digs.split(sep=","))

d = digs.split(sep=",")

print(", ".join(d))

print("   abc   \n".strip())
print("   abc   \n".rstrip())
print("   abc   \n".lstrip())
