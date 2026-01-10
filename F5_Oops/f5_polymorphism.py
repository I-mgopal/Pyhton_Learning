#Overriding Methods in Python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

obj1 = Animal()
obj2 = Dog()
obj2.speak()  # Outputs: Dog barks
obj1.speak()  # Outputs: Animal speaks


#Duck Typing in Python
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
def make_sound(animal):
    animal.sound()
cat = Cat()
cow = Cow() 
make_sound(cat)  # Outputs: Meow