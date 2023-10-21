import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")

penup()  # Lift the pen up
goto(hearta(0), heartb(0))  # Move to the starting position
pendown()  # Place the pen down

for i in range(0, 6000, 3):
    color("#f73487")
    goto(hearta(i) * 20, heartb(i) * 20)
    forward(1)

goto(0, 0)  # Return to the starting position
done()
