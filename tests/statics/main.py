class MyClass:
    def static_method():
        print("MyClass -> static_method")
    pass
    
    def non_static_method(self):
        print("MyClass instance -> non_static_method")
    pass


def main():
    MyClass.static_method() # спрацює
    # MyClass.non_static_method() # не спрацює
    mc = MyClass()
    mc.non_static_method()
    pass

if __name__ == "__main__":
    main()
    



