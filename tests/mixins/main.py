'''
Mixin классы - это классы у которых нет данных, но есть методы. 
Mixin используются для добавления одних и тех же методов в разные классы.
В Python примеси делаются с помощью классов. 
Так как в Python нет отдельного типа для примесей, классам-примесям принято давать имена заканчивающиеся на Mixin.
С одной стороны, то же самое можно сделать с помощью наследования обычных классов, 
но не всегда те методы, которые нужны в разных дочерних классах, имеют смысл в родительском.
'''

class BaseClass:
    @staticmethod
    def test():
        print("BaseClass.test()")

        
class Mixin1:
    @staticmethod
    def test():
        print("Mixin1.test()")


class Mixin2:
    @staticmethod
    def test():
        print("Mixin2.test()")


class MyClass(BaseClass, Mixin1, Mixin2):
    pass
        
        
obj = MyClass()
obj.test()