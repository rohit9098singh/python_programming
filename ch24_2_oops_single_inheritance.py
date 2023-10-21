class employee:
    def __init__(self,name,salary,occupation):
       self.name=name
       self.salary=salary
       self.occupation=occupation

    def showdetails(self):
        print(f"name :{self.name}\nsalary :{self.salary}\noccupation :{self.occupation}")  

class programmer(employee):
    def language_working_on(self):
        print(" pyhton programming language")

e1=employee("rakesh",340000,"hr")
e1.showdetails()
e2=programmer("ram",340000,"rh")     
print("Details of the employee is:")
e2.showdetails()
print("He is working on:")
e2.language_working_on()   
