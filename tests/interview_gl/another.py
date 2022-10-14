class C1:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        

c1 = C1(1, 2, 3, a=1, b=2, c=3)
print(c1.args, c1.kwargs)