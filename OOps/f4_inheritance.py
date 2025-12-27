'''class Parent:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Name: {self.name}")
    

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

obj = Parent("Alice")
obj1 = Child("Bob", 25)
obj.display()
obj1.display()'''

'''#Single inheritance
class Parent:
    def show(self):
        print("This is Paret Class")

class Child(Parent):
    pass

obj1 = Child()
obj1.show()'''


'''#Multilevel
class Grandparent:
    def gp(self):
        print("This is GrandParent")

class Parent(Grandparent):
    def p(self):
        print("This is Parent")

class Child(Parent):
    def c(self):
        print("This is Child")

obj1 = Child()
obj1.c()
obj1.p()
obj1.gp()'''


'''#Multiple 
class Father:
    def f(self):
        print("F class")
class Mother:
    def m(self):
        print("M class")

class Child(Father, Mother):
    pass

obj1 = Child()
obj1.f()
obj1.m()'''

#Hierarchical Inheritance
class Parent:
    def p(self):
        print("About Hierarchichal inheritance")

class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.p()
obj2.p()