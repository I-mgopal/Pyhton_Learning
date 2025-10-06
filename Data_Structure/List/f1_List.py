a = [12,13.2,12,14]

#indexing
print(type(a[1]))
print(a[1])

print("\n --------------Slicing--------------")
#Slicing
b = a[0:len(a)+1]
c = a[-1:-5:-1] #[-1,-(length+1),-1] or default[::-1]
print(b)
print(a is b)
print(c)

print("\n --------------Traversing--------------")
# #using index
for i in range(0,len(a)):
    print(a[i])
print("----------------------------------------")
#Using direct acess
for i in a:
    print(i)

print(dir(list))
help(list)