def calculate(a, b):
    return a + b, a * b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

addition, multiplication = calculate(a, b)

print("Addition:", addition)
print("Multiplication:", multiplication)
