dictonary_varible={'name':"alice",'age':45,'eligible':'true','salary':500000}
print(dictonary_varible)
print(dictonary_varible['name'])
print(dictonary_varible.get('eligible'),('salary'))
print(dictonary_varible.get('eligible'))

print(dictonary_varible.keys())
print(dictonary_varible.values())

for i in dictonary_varible.keys():
    print(i,dictonary_varible[i])

for i in dictonary_varible.values():
    print(i)

for i in dictonary_varible.keys():
    print(f"the value of the correspomding to the  key  {i} is {dictonary_varible[i]}")

print("printing all the key value pair using the items() method")
print(dictonary_varible.items())    
        
