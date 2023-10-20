from functools import reduce
number=[1,2,3,4,5]
sum=reduce[lambda x,y:x+y,number]

# reduce kya karega ke sabse pehle 1+2=3,then 3+3=6, then 6+4=10, then 10+5=15.
