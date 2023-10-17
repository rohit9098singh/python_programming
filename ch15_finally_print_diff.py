def differnce_of_finally_print():
    try:
        value=int(input("enter the size of an array of your choice :"))
        return 1

    except ValueError as e:
        print(e)
        return 0
    
    print("i will always exceute") 
x=differnce_of_finally_print()
print(x)   

'''IN THE ABOVE PROGRAMME PRINT STATEMENT WILL NOT EXECUTE BUT IF THERES FINNALY THEN IT WILL EXEUTE THIS IS WHERE THE DIFFERENCE BETWEEN FINALLY AND PRINT COMES INTO THE PICTURE '''

# but at down it will execute the  print statement writtten inside the finally block
def differnce_of_finally_print():
    try:
        value=int(input("enter the size of an array of your choice :"))
        return 1

    except ValueError as e:
        print(e)
        return 0
    
    finally: print("This line will always execute whether an exception occurs or not.")
x=differnce_of_finally_print()
print(x)   
