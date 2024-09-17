class Employee:
    def read(self):
        self.name=input("Enter name: ")
        self.depart=input("Enter department: ")
        self.salary=int(input("Enter salary: "))
    def display(self):
        print("Your name is ",self.name,". You are from ",self.depart,". Your salary is ",self.salary)
obj1=Employee()
obj1.read()
obj1.display()
