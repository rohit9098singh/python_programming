'''When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. 
              In multiple inheritances, all the features of the base classes are inherited into the derived class.'''

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"name={self.name}") 
        print(f"salary={self.salary}")


class manager:
    def __init__(self, name, department): 
        self.name = name
        self.department = department          

    def display(self):
        print(f"name={self.name}")
        print(f"department={self.department}")


class superviser(employee, manager):
    def __init__(self, name, salary, department):
        employee.__init__(self, name, salary)
        manager.__init__(self, name, department)

    def display2(self):
        self.show()  
        self.display() 

superv = superviser("Juli", 50000, "Human Resources")
superv.display2()
