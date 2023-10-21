class Employee:
    def __init__(self, name, department, location, age):
        self.name = name
        self.department = department
        self.location = location
        self.age = age

    @property
    def getname(self):
        return self.name

    @getname.setter 
    def setname(self, name):
        self.name = name

    @property
    def getdepartment(self):
        return self.department

    @getdepartment.setter
    def setdepartment(self, department):
        self.department = department

    @property 
    def getlocation(self):
        return self.location

    @getlocation.setter
    def setlocation(self, location):
        self.location = location  

    @property
    def getage(self):
        return self.age

    @getage.setter
    def setage(self, age):
        self.age = age

# Creating an instance and using setters to modify the attributes
rakesh = Employee("John Doe", "Manager", "New York", 45)
rakesh.setname = "rohit"
rakesh.setdepartment = "hr"
rakesh.setlocation = "banglore"
rakesh.setage = 54

# Getting and printing the details using getters
print("name:", rakesh.getname)
print("department:", rakesh.getdepartment)
print("location:", rakesh.getlocation)
print("age:", rakesh.getage)

