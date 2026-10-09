class A:
    def display(self):
        print("This is class A")

class B(A):
    def show(self):
        print("This is class B")

class C(A):
    def show1(self):
        print("This is class C")

class D(B, C):
    def result(self):
        print("This is class D")

obj = D()
obj.display()
obj.show()
obj.show1()
obj.result()
