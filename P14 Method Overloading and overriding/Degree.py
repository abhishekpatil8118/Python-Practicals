class Degree:
    def getDegree(self):
        print("I got a Degree")
class Undergraduate(Degree):
    def under(self):
        print("I am Undergraduate.")
class Postgraduate(Degree):
    def under(self):
        print("I am Postgraduate.")
obj1=Degree()
obj2=Undergraduate()
obj3=Postgraduate()
obj1.getDegree()
obj2.under()
obj3.under()
