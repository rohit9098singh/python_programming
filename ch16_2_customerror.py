
class zerodivide(Exception):
    pass
try:
    i=int(input("enter the number of your choice\n"))
    if(i==0):
        raise zerodivide
    else:
        print("the input number when it is divided by 10 the result is :",int(10/i))
except zerodivide:
    print("input value is zero please enter another value")
