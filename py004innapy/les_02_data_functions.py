def lesson02():
    a = 7
    a = 6.7
    b = 'hi'
    b = 0
    b = -23.1
    print(a)
    var_a = 'hello'
    print(var_a, a, b)

    a = b = c = 0
    print(a, b, c)
    print(id(a))
    print(id(b))
    print(id(c))

    a, b = 1, 2
    print(id(a), id(b))

    a, b = 1, 2
    print(a, b)
    a, b = b, a
    print(a, b)
