class Parent1:
    def fun1(self):
        print("Class Parent1")
class Parent2:
    def fun2(self):
        print("Class Parent2")
class Child(Parent1,Parent2):
    def fun3(self):
        print("Class Child")
obj1=Child()
obj1.fun1()
obj1.fun2()
obj1.fun3()
