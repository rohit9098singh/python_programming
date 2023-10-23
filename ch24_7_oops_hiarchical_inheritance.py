class Animal:
    def who_am_i(self):
        print("I am an animal.")


class Dog(Animal):
    def bark(self):
        print("Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow!")


# Creating objects of the derived classes
dog = Dog()
cat = Cat()

# Accessing methods
dog.who_am_i()  # Accessing method from the base class
dog.bark()  # Accessing method from class Dog
cat.who_am_i()  # Accessing method from the base class
cat.meow()  # Accessing method from class Cat
