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
