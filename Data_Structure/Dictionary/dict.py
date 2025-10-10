d = {1:10,2:20}
print(type(d))

# Acess value by using key/read
print(d[1])

#Update
d[1] = 1000
print(d)

#Create
d.update({3:30})
d[4] = 40
print(d)

# Deleting
del d[3]
print(d)


#Traversing
dict = {1:10,2:20,3:30,4:40}
for i in dict:
    print(i, ":", dict[i])
#acess values
for i in dict.values():
    print(i)

#Methods
d.clear()
print(d)

