def sum_calculation(*args):
    total=0
    for i in args:
        total=total+i

    print("total of the provided argument is as follow :",total)
print("==========performing  the variable_length_argument============")
sum_calculation(1,2,3,4,4)
sum_calculation(34,43,22,121,3,452,2324,2311)


