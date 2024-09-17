class Parent:
    def fun1(self):
        self.roll=int(input("Enter roll no: "))
        self.name=input("Enter name: ")
class Child(Parent):
    def fun2(self):
        print("Roll Number: ",self.roll)
        print("Name: ",self.name)
obj1=Child()
obj1.fun1()
obj1.fun2()
