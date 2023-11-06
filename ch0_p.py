class student:
    def __init__(self):
        self._name="harry"
    def _funname(self):
        return "code with harry"    
    
class subject(student):
    pass

object=student()
obj=subject()
print(obj._name)
print(obj._funname())
print(object._name) 
print(object._funname())      