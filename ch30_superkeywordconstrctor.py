class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(f"name={self.name} age={self.age} salary={self.salary}")    

class programmer(employee):
    def __init__(self,name,age,salary,location):
        super().__init__(name,age,salary) 
        self.location=location

    def display(self):
      print(f"name={self.name} age={self.age} salary={self.salary} location={self.location}")

rohit=employee("rohit",34,35000)
riya=programmer("rohit",34,35000,"jamshedpur") 
rohit.display()
riya.display()              

