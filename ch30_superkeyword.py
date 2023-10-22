class employee:
    def parent_method(self):
        print("this is a parent method..")
class child(employee):
    def parent_method(self):
       print("i am child class parent method")
        
    def child_method(self):
       print("we are inside the child method......")
       super().parent_method()
c=child()
c.child_method()
c.parent_method()
            