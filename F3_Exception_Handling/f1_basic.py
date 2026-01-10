num1 = int(input("Enter your first value- "))
num2 = int(input("Enter your seconde value- "))

try:
    (num1//num2)
except ZeroDivisionError:
    print("You can't divide by 0")
else:
    print(f"Ans is {num1//num2}")


num3 = input("Enter your number:- ")
try:
    (num1/num2)
    (num1/num3)
except Exception as err:
    print(f"There is an Error as {err}")
else:
    print(f"Ans is {num1//num2}")
finally:
    print("No matter what it will run")


# Create your own Exception
age = int(input())
if age < 10 or age>18:
    raise ValueError("Age must be between 10 and 18")
else:
    print("Welcome to club")