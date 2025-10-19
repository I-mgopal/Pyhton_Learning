#Input
name = input("Enter your name: ")
age = int(input("What is your age?: "))

#Output
print(f"Hi, I am {name}, Welcom to this File.")
print(f"My name is {name} and my age is {age}.")

#Multiple input using oneline
list1 = list(map(int,input("Enter list elements: ").split()))
print(list1)