class employee:
    company="APPLE"
    def show(self):
        print(f"the name of the employee is {self.name} and he is working in {self.company}")

    @classmethod
    def change_company(cls,newcomapny):
        cls.company=newcomapny
e1=employee()
e1.name="raghu"
e1.show()

e2=employee()
e2.name="ramesh"
e2.show()
e2.change_company("TESLA")
e2.show()

print(employee.company)
      