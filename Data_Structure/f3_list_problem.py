#Q1. Print positive elements and then negative elements

list1 = [1,3,2,10,-2,-4,4]
print("All positiv elements: ")
for i in list1:
    if(i>=0):
        print(i)
print("All positiv elements: ")
for i in list1:
    if(i<0):
        print(i)


#Q2.Mean of list elements
sum = 0
for i in list1:
    sum+=i

mean = sum//len(list1)
print(len(list1)) 
print(f"mean is {mean}")



#Q3. Greatest element and index also
list2 = [1,2,5,6,2,7,7]
max1 = 0
for i in list2:
    if(i>=max1):
        max1 = i
print(f"Greatest element is {max1} and index is {list2.index(max1)}")

# Q4. Find the seconde largest elements 
list3 = [4,3,2,1]
max1 = 0
second_max = 0
for i in list3:
    if(i >= max1):
        second_max = max1
        max1 = i
    elif(i>second_max and i<max1):
        second_max = i

print(f"Second largest element is {second_max}")


#Q5. Check list is sorted or not
list4 = [1,2,6,4,5]
for i in range(0,len(list4)-1):
    if(list4[i]>list4[i+1]):
        print("List is not sorted")
        break
else:
    print("List is sorted")