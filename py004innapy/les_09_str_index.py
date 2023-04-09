s = "hello python"
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])

print(s[0:5])
print(s[3:5])

s = "abc"
print(s[1:2])  # last index not included
print(id(s))
print(id(s[:]))

s = "abcdefgh"
print(s[1:7:2])  # bdf

a = "abc"
print(a[::-1])  # inverted

s1 = "hello"
s2 = "H" + s1[1:]
print(s2)
