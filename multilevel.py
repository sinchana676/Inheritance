class Grandfather:
    def display1(self):
        print("This is the grandfather class")

class Father(Grandfather):
    def display2(self):
        print("This is the father class")

class Child(Father):
    def display3(self):
        print("This is the child class")

obj = Child()
obj.display1()
obj.display2()
obj.display3()
