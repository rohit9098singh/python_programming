from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("done for 20")
print(fx(30))
print("done for 30")
print(fx(40))
print("done for 40")
print(fx(50))
print("done for 50")

#this part will not take much time to execute at here
print(fx(20))
print("done for 20")
print(fx(30))
print("done for 30")
print(fx(40))
print("done for 40")
print(fx(50))
print("done for 50")