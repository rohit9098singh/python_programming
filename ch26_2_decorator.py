import time
def ticktok(func):
    def wrapper():
        t1=time.time() # Records the current time before the function is executed.
        func()
        t2=time.time()-t1# Calculates the time taken to execute the function by subtracting the start time from the current time.
        print(f"function {func.__name__} ran in {t2} second")
    return wrapper

@ticktok   # THE OBOVE LINE BASICALLY SAYS KE NEECHE WAALE FUNCTION KO TICKTOK NAM WAALE FUNCTION ME PASS KAR DO OR TAKI VO ADDITIONAL CODE KE SATH CHAL SAKE 
def do_this():
    time.sleep(1.3)

@ticktok    
def do_that():
    time.sleep(1.4)

do_this()
do_that()
print("done")            

    