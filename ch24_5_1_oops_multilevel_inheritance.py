class animal:
    def __init__(self,species):
        self.species=species

    def speak(self):
        print("i am a general animal")

class mammal(animal):
    def __init__(self,species,sound):
        super().__init__(species)
        self.sound=sound
    def speak(self):
        return self.sound

class dog(mammal):
    def __init__(self,breed,sound):
        super().init("dog",sound)    
        self.breed=breed    

