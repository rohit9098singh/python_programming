f=open('myfile3.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0]) # now if *2 then it does as we have typecasted it
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"mark of student {i} in math is {m1*2}")#note if i use {m1*2} then it will print 6767 because it is a string so we need to typecaste it
    print(f"mark of student {i} in sst is {m2}")
    print(f"mark of student {i} in english is {m3}")
    print(line)
    