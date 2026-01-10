#Q1. Accept two numbers and print the greatest between them
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Seconde Number: "))
if(num1>num2):
    print(f"Greatest number is num1 {num1}")
elif (num1 == num2):
    print("Both the numbers are same")
else:
    print(f"Greatest number is num2 {num2}")

#Q2. Accept gender as character based on this print respecive greeting message
gender = input("Enter Gender either M/F: ")
if(gender == 'M' or gender == 'm'):
    print("Good Morning Sir")
elif(gender == 'F' or gender=='f'):
    print("Good Morning Mam")
else:
    print("Enter Wrong charcter")

# Q3. Check enter Integer odd or even
num3 = int(input("Enter a number: "))
if(num3 %2 == 0):
    print("Number is even")
else:
    print("Number is Odd")

#Q4. Accep the name and age and check valid vother or not
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if(age>=18):
    print(f"hello {name} you are a valid voter")
else:
    print(f"hey {name} you are not a valid voter")

#Q5. Accept year and check is it a valid year or not
year = int(input("Enter a year: "))
if(year%400 ==0):
    print(f"{year} is Leap year")
elif(year%4==0 and year%100!=0):
    print(f"{year} is Leap year")
else:
    print(f"{year} is not Leap year")

## if-elif ladder
temp = int((input("Enter the temparature in celsius: ")))
if(temp < 0):
    print("Freezing Cold")
elif (temp>=0 and temp<10):
    print("Very Cold")
elif (temp>=10 and temp<20):
    print("Cold")
elif (temp>=20 and temp<30):
    print("Pleasant")
elif (temp>=30 and temp<40):
    print("Hot")
else:
    print("Very Hot")