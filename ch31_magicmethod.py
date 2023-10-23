class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else:
            return f"{self.real} + {self.imag}i"
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)    


# Testing the class
if __name__ == '__main__':
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -1)

    print("Complex Number 1:", c1)
    print("Complex Number 2:", c2)

    sum_result = c1 + c2
    print("Sum of the complex numbers:", sum_result)

    sub_result = c1 - c2
    print("Difference of the complex numbers:", sub_result)

    mul_result = c1 * c2
    print("Product of the complex numbers:", mul_result)

    equality_check = c1 == c2
    print("Equality of the complex numbers:", equality_check)

    conjugate_c1 = c1.conjugate()
    print("Conjugate of Complex Number 1:", conjugate_c1)
        
'''In the provided code, when you write c1 + c2 or c1 - c2, it actually calls the __add__ or __sub__ method defined in the class 
ComplexNumber respectively. This behavior is part of how Python works with operators.

When you write c1 + c2, Python interprets it as c1.__add__(c2), and when you write c1 - c2, Python interprets it as c1.__sub__(c2). 
These special methods are called automatically when the corresponding operators are used with instances of the class.

Similarly, when you print an object using the print function, it calls the __str__ method of that object. So, when you write print(c1),
 it is equivalent to print(c1.__str__()). This allows you to customize how an object is printed.'''        