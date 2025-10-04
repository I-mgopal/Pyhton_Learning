# Reverse a number using while loop, and check is it palindrome or not

num1 = int(input("Enter the number: "))
temp = num1
if num1<0:
    sign = -1
    num1 = abs(num1)
else:
    sign = 1

rev = 0

while num1:
    digit = num1%10
    rev = rev * 10 + digit 
    num1 = (num1//10)

rev *= sign
print(f"Reverse of {temp}, is {rev}")


if temp==rev:
    print(f"{temp} is a plaindrome")
else:
    print(f"{temp} is not palindrome")