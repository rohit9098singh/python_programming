class A:
    def method_a(self):
        print("Method A")


class B(A):
    def method_b(self):
        print("Method B")


class C(A):
    def method_c(self):
        print("Method C")


class D(B, C):
    def method_d(self):
        print("Method D")


# Creating an object of class D
obj_d = D()

# Accessing methods
obj_d.method_a()  # Accessing method from class A
obj_d.method_b()  # Accessing method from class B
obj_d.method_c()  # Accessing method from class C
obj_d.method_d()  # Accessing method from class D
