

def double(a):
    return a * 2
print(double(5))

# --> PASSING A FUNCTION INTO ANOTHER FUNCTION 
def appl(fx, value):
    return 6 + fx(value,value)  # Modified to pass appropriate arguments

def appl2(fx, value):
    return 6 + fx(value) 
# or
double = lambda x: x * 2  # both are meaningfully the same
print(double(3))

# or
avg = lambda a, b: (a + b) / 2  # multiple argument one
print(avg(45, 76))

# printing the function inside function value
print(appl(avg, 4)) 
print(appl2(lambda x:x*2,5)) 
