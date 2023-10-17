def fibonacci(n):
    if(n==1 or n==2):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
value=int(input("enter the number of which the fibonaci series is to be calclated :"))
t=fibonacci(value)
print(t)
