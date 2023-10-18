def add(a,b):
    c =a+b
    return c
def subtract(a,b):
    c=a-b
    return c
  
def multiplication(a,b):
    c=a*b
    return c
   
def divide(a,b):
    c=a/b
    return c
    
#a, b = map(int, input("Enter the value of a and b separated by space: ").split())# this function is used to take multiple input at a time
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if __name__=="__main__":
  print(a,b)
  print(add(a,b))
  print(subtract(a,b))
  print(multiplication(a,b))
  print(divide(a,b))

      
    