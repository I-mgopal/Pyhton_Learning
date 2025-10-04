def greet():
    print("Hello Welcome here!")

greet()

# Positional Argument
def sum(a,b): # Parameter
    print(f"sum of two number is {a+b}")

sum(12,13) # Agument

# Default Argument
def mult(first,second=3):
    print(f"Multipication is {first*second}")

mult(2) #default
mult(2,4) #Override

#Keyword Argument
def intro(name,age):
    print(f"My name is {name}, and age is {age}")

intro(age=21,name='John')


#Q1. Palindrome or not using fun

def palindrome(str):
    rev = str[::-1]
    if(rev == str):
        print(str,"is a palindrome")
    else:
        print(str,"is not a palindrome")

str = input("Enter a string: ")
palindrome(str)