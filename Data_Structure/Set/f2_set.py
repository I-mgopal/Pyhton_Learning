a = {1,2,3}
b = {3,4,5}
#print all common
unioun_set = a.union(b) # or (a|b)
print(unioun_set)

#Print only common value
intersection_set = a.intersection(b) # or (a&b)
print(intersection_set)

# Show sets value
difference_set = a.difference(b) # or (a-b) 
#(b-a) value give the vale present in b
print(difference_set)

# remove common part
symmetric_diff = a.symmetric_difference(b) #or (a^b)
print(symmetric_diff)
