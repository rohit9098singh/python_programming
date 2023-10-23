class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return "Generic animal sound"


class Mammal(Animal):
    def __init__(self, species, sound):
        super().__init__(species)
        self.sound = sound

    def speak(self):
        return self.sound


class Dog(Mammal):
    def __init__(self, breed, sound):
        super().__init__("Dog", sound)
        self.breed = breed


class Labrador(Dog):
    def __init__(self, color):
        super().__init__("Labrador", "Bark")
        self.color = color


# Creating instances of the classes
dog = Dog("Poodle", "Woof")
labrador = Labrador("Golden")

# Using the instances
print(f"I am a {dog.species} of breed {dog.breed}. I say {dog.speak()}.")
print(f"I am a {labrador.color} {labrador.species} of breed {labrador.breed}. I say {labrador.speak()}.")
