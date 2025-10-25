class Factory:
    a = 12 #attribute
    def hello(self): #method
        print("This is method")

print(Factory().a)
Factory().hello()

class Dog:
    def __init__(self, name, age):  # Constructor method
        self.name = name
        self.age = age

    def bark(self):  # Instance method
        return f"{self.name} says woof!"
