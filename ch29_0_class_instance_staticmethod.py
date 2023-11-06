class student:
    school="telusko" # school is a class variable and if we want to use the class varible we should make a class method to access it with (cls) in bracket
    def __init__(self,m1,m2,m3):  # writing self means it belogs to a particular object that is insatnce variable
        self.m1=m2
        self.m2=m2
        self.m3=m3
    def average(self):
        return int((self.m1+self.m2+self.m3)/3) 
    
    @classmethod    # if we dont provide this it will generate an error it is basically a type of a decorater only 
    def getschool(cls):
        return cls.school 
    @staticmethod
    def info(): #this is not related to object not related to class ok so it is empty at here this is only what the static method is
        print("this is a student class.....in rohit module")
s1=student(88,89,90)
s2=student(90,77,85)
print(s1.average())
print(s2.average())
print(student.school) # here we have called it with school dot not with s1. or s2. because it should not work for a single object right rather for all 

'''calling the static methods at here'''
student.info() #since it is a static methods we dont need a object to call it we can call it direcctlt at here 

'''static methods if we want to do some extra with the class then we use static methods just because it is not associated with class or any objects'''