num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
<<<<<<< HEAD
choice = input("Enter choice (+, /): ")

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b

def subtract(a, b):
    return a - b

if choice == '+':
    print(f"Result: {add(num1, num2)}")
=======
choice = input("Enter choice (+,-,*,/): ")

def multiply(a, b):
    return a * b

if choice == '+':
    print(f"Result: {add(num1, num2)}")
elif choice == '-':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '*':
    print(f"Result: {multiply(num1, num2)}")
>>>>>>> origin/乘法
elif choice == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")
