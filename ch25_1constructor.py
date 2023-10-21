class detail:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def info(self):
        print(f"the person name is {self.name} and he is {self.occupation}")  

person1=detail("rahul","developer")
person2=detail("aman","sweeper")
person1.info()
person2.info()      
 

    