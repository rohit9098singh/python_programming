'''class person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def fromstring(cls,string):
        name,age=map(str.strip,string.split("-"))  
        return cls(name,int(age))
    def display(self):
        print(f"name={self.name} age={self.age}")

def main():
    new_string=input("enter the string of your choice")
    p=person1.fromstring(new_string)


    print("details of the created employee is as follow")
    p.display()

    if __name__=='__main__':
      main()
    '''
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromstring(cls, string):
        name, age = map(str.strip, string.split("-"))  
        return cls(name, int(age))

    def display(self):
        print(f"name={self.name} age={self.age}")

def main():
    string = input("Enter the string of your choice: ")
    p = person1.fromstring(string)

    print("Details of the created employee are as follows:")
    p.display()

if __name__ == '__main__':
    main()
