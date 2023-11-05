# Defining the base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Defining a derived class that inherits from the Vehicle class
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


# Creating an instance of the Car class
car = Car("Toyota", "Camry", 2022, 4)

# Accessing the properties and methods of the base and derived classes
car.display_info()
