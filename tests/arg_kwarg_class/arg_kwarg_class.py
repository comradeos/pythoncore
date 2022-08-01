class MyClass:
    def __init__(self, *args, **kwargs):
        self.a = args
        self.b = kwargs


copy = MyClass(25, 34, 43, 52, a=250, b=340, c4=430)
print(copy.a)
print(copy.b)
