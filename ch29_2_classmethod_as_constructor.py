
class person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
       name,salary=string.split("-")
       return cls(name,int(salary))   

e = person("rahul", 122900)
print(e.name)
print(e.salary)

string = "harry-12000"
e1 = person.fromstr(string)
print(e1.name)
print(e1.salary)