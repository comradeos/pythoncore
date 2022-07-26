x = 10
y = 11


if x > y:
    print('x > y')
elif x == y:
    print('x = y')
elif x < y:
    print('x < y')
else:
    print('What?')


print(10 < 20 and 20 < 30)
print(10 < 20 < 30)


def is_even(number:int)->bool:
    if number % 2 == 0:
        return True
    return False

print(is_even(11))