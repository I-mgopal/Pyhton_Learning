a = (1,2,3,4,6,7,7,7)

#Traversing
for i in a:
    print(i," ")

# Methods
index = a.index(4)
print(f"Index of 4 is {index}")
count = a.count(7)
print(f"Total number of counts of 7 are {count}")

# Tuple unpacking
c,d = (1,2,)
print(type(c))
print(c)
print(type(d))
print(d)

b = (1,)
print(type(b))

