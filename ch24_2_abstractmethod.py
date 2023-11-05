from abc import ABC, abstractmethod

# Defining an abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Creating a subclass that inherits from the abstract class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Creating an instance of the Square class
square = Square(5)

# Calling the methods of the Square class
print("Area of the square:", square.area())
print("Perimeter of the square:", square.perimeter())
