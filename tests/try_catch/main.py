def div(a :int, b :int) -> int:
    return a / b

try:
    res1 = div(1, 1)
except:
    res1 = 5

try:
    res2 = div(1, 1)
except:
    res2 = 5

res3 = res1 + res2

print(res3)