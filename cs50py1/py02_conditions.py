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



def main()->None:
    number=int(input('Number? '))
    if is_even(number):
        print('Even')
    else:
        print('Odd')
        


def is_even(number:int)->bool:
    return number % 2 == 0



main()