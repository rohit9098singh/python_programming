
class zerodivide(Exception):
    pass
try:
    i=int(input("enter the number of your choice\n"))
    if(i==0):
        raise zerodivide
except zerodivide:
    print("input value is zero please enter another value")
    print()