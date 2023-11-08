
if __name__ == '__main__':
    n = int(input("enter your number so that it could be checked :").strip())
    if(n%2!=0):
        print("weird")
    else:
        if (2<=n<=5):
            print("not weired")
        elif(6<=n<=20):
            print("weired")
        else:
            print("not weired") 