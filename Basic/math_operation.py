import math

def add(a, b):
    result = int(a) + int(b)
    print(f"Sum of {a} and {b} is {result}")

def subtract(a, b):
    result = int(a) - int(b)
    print(f"Difference between {a} and {b} is {result}")

def multiply(a, b):
    result = int(a) * int(b)
    print(f"Product of {a} and {b} is {result}")

def divide(a, b):
    if int(b) == 0:
        print("Error: Cannot divide by zero.")
    else:
        # Integer division truncates the decimal part (e.g., 10 / 3 = 3)
        result = int(int(a) / int(b))
        print(f"Division of {a} by {b} (integer result) is {result}")

def modulus(a, b):
    if int(b) == 0:
        print("Error: Cannot perform modulus by zero.")
    else:
        result = int(a) % int(b)
        print(f"Modulus (remainder) of {a} divided by {b} is {result}")

def sqrt(a):
    if int(a) < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        # Calculates the square root and converts the float result to an integer
        result = int(math.sqrt(int(a)))
        print(f"Square root of {a} (integer result) is {result}")
