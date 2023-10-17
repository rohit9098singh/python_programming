def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))
    
num=int(input("\nenter the number whoes factorail is to be calculated :"))
value=factorial(num)
print("the factorail of the given number is :",value)    