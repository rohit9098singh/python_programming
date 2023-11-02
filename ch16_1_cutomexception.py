class invalideageexception(Exception):
    pass
number=18
try:
        n=int(input("enter the age of your choice but make you have to guess and it mactch with the original no :"))
        if(n<number ):
              raise invalideageexception
        else:
              print("you are eligible to vote")

except invalideageexception :
    
    print("invalid entery your age is less")  