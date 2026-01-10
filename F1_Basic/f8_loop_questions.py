#Q1. Accept an integer and print hello n times
num1 = int(input("Enter the nmber: "))
for i in range(num1):
    print("Hello World")

#Q2. print natural number upto n
for i in range(1,num1+1):
    print(i)

#Q3. Reverse the n to 1
for i in range(num1,0,-1):
    print(i)

#Q3. Sum of n terms
sum = 0
for i in range(1,num1+1):
    sum += i
print(f"Sum of {num1} is {sum}")

#Q4. print the factors of  a number
for i in range(1,num1+1):
    if(num1 % i == 0):
        print(f"{i} is factor of {num1}")

#Q5. Print Number is prime or not
import math
for i in range(2,int(math.sqrt(num1))+1):
    if(num1%i == 0):
        print(f"{num1} is not a prime number")
        break
else:
    print(f"{num1} is a prime number")


#Q5. Reverse a string
a = "Sheriyan"
print(a[::-1])

#Q6. Count all letters, digits, and special Symbol
str1 = "P@#yn26at^&i5ve"
char = 0
digit = 0
spchr = 0
for i in str1:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1

print(f"Your total numbers of digits: {digit}\n Your total numbers of char: {char}\n Your total numbers of spchar: {spchr}")