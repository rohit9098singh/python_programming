class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self.__year = year  # Private attribute

    # Getter method to access private attribute
    def get_year(self):
        return self.__year

    # Setter method to modify private attribute
    def set_year(self, year):
        self.__year = year


# Creating an object of the Car class
car = Car("Toyota", "Camry", 2022)

# Accessing the protected attributes
print(car._make)  # Output: Toyota
print(car._model)  # Output: Camry

# Trying to access the private attribute directly will result in an AttributeError
# print(car.__year)  # This line will throw an AttributeError

# Using getter method to access the private attribute
print(car.get_year())  # Output: 2022

# Using setter method to modify the private attribute
car.set_year(2023)
print(car.get_year())  # Output: 2023
