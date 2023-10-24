from functools import lru_cache
@lru_cache (maxsize=None)
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#first calling of the function    
print(fibonacci(5))
#second calling of the function
print(fibonacci(5) )  
    