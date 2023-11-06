class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The name of the person is: {self.name} and is = {self.age} years old.")

    @property
    def details(self):
        return self.name, self.age

    @details.setter
    def details(self, values):
        self.name, self.age = values

# Creating instances and calling methods
obj1 = Person("rohit", 45)
obj1.show()
obj2 = Person("ram", 54)
obj2.details = ("riya", 44)
print(obj2.details)
obj2.show()
