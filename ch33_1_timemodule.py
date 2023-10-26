import time

def usingfor():
    for i in range(200):
        print(i+20)

def usingwhile():
    i = 0  # Initialize i here
    while i < 200:
         print(i) 
         i = i + 35
      

start_time = time.time()
usingfor()
end_time = time.time()
print("Time taken by usingfor:", end_time - start_time)

start_time = time.time()
usingwhile()
end_time = time.time()
print("Time taken by usingwhile:", end_time - start_time)

#USING THE TIME.SLEEP METHODS
a = input("Enter the value of a: ")
print(a)
time.sleep(2)
print("Printing this message after 2 seconds")

#USING THE TIME.STRFTIME METHODS
t=time.localtime()
#formated_time=time.strftime("%y-%m-%d  %H:%M:%S",t)
print(t)
