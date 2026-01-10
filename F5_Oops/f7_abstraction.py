# Abstraction is the process of hiding implementation details and showing only the essential features to the user.
# In short:
# Focus on what an object does, not how it does it.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape): 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

obj = Rectangle(5, 10)
print("Area of Rectangle:", obj.area())            # Outputs: Area of Rectangle: 50 
print("Perimeter of Rectangle:", obj.perimeter())  # Outputs: Perimeter of Rectangle: 30