class vechile:
    def __init__(self,name):
        self.name=name

    def display(self):    
       print(f"name of the vechile{self.name}")    

class car(vechile):
    def __init__(self,name,colour):
        super().__init__(name)
        self.colour=colour
    def display(self):
        print(f"name={self.name} and colour ={self.colour}")         


class electriccar(car):
     def __init__(self,name,colour,battery_capacity):
              super().__init__(name,colour)
              self.battery_capacity=battery_capacity

     def display(self):
              print(f"name = {self.name} colour={self.colour} and its battery_capacity is {self.battery_capacity}")   

obj1=electriccar("baleno","blue","4_hours")
obj2=car("baleno","blue")
obj3=vechile("vechile")
obj1.display()
obj2.display()
obj3.display()                