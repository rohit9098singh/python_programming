import datetime 
res=datetime.datetime.now()
print(res)

#creating the date time constructor at here similar think as we are here making its object
res1=datetime.datetime(2023,5,22,4,45,54,43222)
print(res1)

res3 = res.strftime("%Y")
print("full version of the year is", res3)
res3 = res.strftime("%B")
print("full version of the month is", res3)
res3 = res.strftime("%A")
print("full version of the day is", res3)
res3 = res.strftime("%M")
print("time in minute is", res3)
res3 = res.strftime("%S")
print("time in second is", res3)
res3 = res.strftime("%f")
print("milliseconds is", res3)
#The output will provide the current date and time in the first print statement, and then it will create 
# a specific datetime object and print it. The subsequent lines use the strftime method to format the datetime object in 
# different ways, such as getting the year, month, day, minute, second, and milliseconds.

print("===================================================")
res3 = res.strftime("%y")
print("short version of the year is", res3)
res3 = res.strftime("%w")
print("shot version of the month is", res3)
res3 = res.strftime("%a")
print("shot version of the day is", res3)
res3 = res.strftime("%M")
print("time in minute is", res3)
res3 = res.strftime("%S")
print("time in second is", res3)
res3 = res.strftime("%f")
print("milliseconds is", res3)
res3=res.strftime("%I")
print("total hours are ",res3)
res3=res.strftime("%p")
print("AM/PM are ",res3)

print("==========strftime in one=============================")
res4=res.strftime("%y-%m-%d  %H:%M:%S")
print(res4)
res4=res.strftime("%y-%w-%a %H:%M:%S:%f") # execute and check whats the difference between all that
print(res4)

