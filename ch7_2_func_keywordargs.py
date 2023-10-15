def personal_details(fname,middleName,lastName,phoneno):
    print("hello", fname, middleName, lastName, "\nphone no:", phoneno)

print("============showing you the example of keyword argument===========\n")
personal_details(fname='rohit',lastName='singh',middleName='kumar',phoneno='831203')
print()    

personal_details(phoneno='203',lastName='singh',fname='rohit',middleName='yadav')
print()