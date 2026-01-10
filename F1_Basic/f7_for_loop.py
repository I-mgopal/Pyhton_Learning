#For loop
#Q1. Basic For loop
for i in range(11):
    print(i)

print("----------------------")
#Q2. Reverse order
for i in range(16,0,-1):
    print(i)

print("----------------------")
#Q3. Print a table of 5
for i in range(1,11):
    print(f"{5} * {i} = {5*i}")

# OR

for i in range(5,51,5):
    print(i)


print("----------------------")
#Loops for String
#using index value
a = "Gopal"
for i in range(len(a)):
    print(a[i])

print("----------------------")
#Direct run
for char in a:
    print(char)


print("----------------------")
#Break - Else
for i in range(1,21):
    if i==56:
        print("Break statement is run")
        break
    print(i)
else:
    print("Break statement is not run")