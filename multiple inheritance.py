class Father:
    def father(self):
        print("This is the father class")

class Mother:
    def mother(self):
        print("This is the mother class")

class Child(Father, Mother):
    def child(self):
        print("This is the child class")

obj = Child()
obj.father()
obj.mother()
obj.child()
