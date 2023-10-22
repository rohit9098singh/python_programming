class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod #======================ACTING AS ONE KIND OF A CONSTRUCTOR...................
    def fromstr(cls,string):
      name,age=string.split(",")
      return cls(name,int(age))

string="john,34"           
e=person.fromstr(string)
print(e.name,e.age)    
            
