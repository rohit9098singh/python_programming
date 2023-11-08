'''__init__(self, [...]): Constructor method that initializes an instance of a class.
__str__(self): Called by the str() built-in function and returns a string representation of the object.
__repr__(self): Called by the repr() built-in function and returns a string representing the object for inspection.
__len__(self): Called by the len() built-in function and returns the length of the object.
__add__(self, other): Called by the + operator and is used to define the behavior for the addition of two objects.
__sub__(self, other): Called by the - operator and is used to define the behavior for the subtraction of two objects.
__mul__(self, other): Called by the * operator and is used to define the behavior for the multiplication of two objects.
__eq__(self, other): Called by the == operator and is used to define the behavior for equality comparison between two objects.
__lt__(self, other): Called by the < operator and is used to define the behavior for less-than comparison between two objects.
__gt__(self, other): Called by the > operator and is used to define the behavior for greater-than comparison between two objects.
'''
class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'MyClass({self.value})'

    def __str__(self):
        return f'A custom object of MyClass with value: {self.value}'

    def __len__(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

# Creating instances of the class
obj1 = MyClass(10)
obj2 = MyClass(5)

# Using the dunder methods
print(len(obj1))  # __len__ method
print(obj1 + 5)   # __add__ method
print(obj1 - 3)   # __sub__ method
print(obj1 * 2)   # __mul__ method
print(obj1 == obj2)  # __eq__ method
print(obj1 < obj2)   # __lt__ method
print(obj1 > obj2)   # __gt__ method
