def func1():
    try:
        l = [1, 2, 3, 4]
        for item in l:
            print(item)
        i = int(input("Enter the index: "))
        print(l[i])
        return l
    except:
        print("some error occurred")
    finally:
        print("I will be executing always.")
    print("i will never execute")    

x = func1()
print(x)
