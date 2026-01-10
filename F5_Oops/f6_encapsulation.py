class Encapsulation:
    a = "This is a class variable"
    def show(self):
        print("This is a method inside the class")
class Test(Encapsulation):
    def display(self):
        print(super().a)

test_obj = Test()
test_obj.display()  # Outputs: This is a class variable

# Access modifiers in Python
class Student:
    def __init__(self, name, age, marks):
        self.name = name        # Public
        self._age = age         # Protected
        self.__marks = marks   # Private

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Marks: {self.__marks}")



student = Student("Alice", 20, 95)
print(student.name)      # Accessible
print(student._age)     # Accessible (by convention, should be treated as protected)    
# print(student.__marks)  # Not Accessible, will raise AttributeError
student.show_details()