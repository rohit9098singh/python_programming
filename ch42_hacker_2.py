class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

calculator = Calculator()
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print(calculator.add(a, b))
print(calculator.sub(a, b))
print(calculator.mult(a, b))
