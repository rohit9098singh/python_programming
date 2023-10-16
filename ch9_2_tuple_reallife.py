employee1=('joe',34,'banglore','software developer',80000)
employee2=('aman',35,'bihar','mechanical engineer',500000)
employee3=('abhishek',36,'oddisa','labour',90000)
employee4=('rohit',37,'jharkhand','product mgr',450000)

def product_display(employee):
    print(f"name :{employee[0]}\nage :{employee[1]}\nlocation :{employee[2]}\nskilled as :{employee[3]}\nsalary ={employee[4]}")
    print("==============================")


product_display(employee1)
product_display(employee2)
product_display(employee3)
product_display(employee4)

