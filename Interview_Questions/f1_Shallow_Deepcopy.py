import copy
#Shallow copy
list1 = [1,2,3,[1,3]]
list2 = copy.copy(list1)

list2[-1][0]=2
list2[-2] = 8
print(list1)
print(list2)


#Deep copy
list3 = [1,2,3,4,5,[7,7]]
list4 = copy.deepcopy(list3)
list4[-1][0] = 6
print(list3)
print(list4)
