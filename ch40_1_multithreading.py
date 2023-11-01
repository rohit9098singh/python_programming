import threading
import time
def func(seconds):
    print(f"running after {seconds} seconds")
    time.sleep(seconds)
func(3)
func(4)
func(6)    