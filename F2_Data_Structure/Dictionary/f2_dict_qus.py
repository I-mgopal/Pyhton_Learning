# Merge two dictionary
d1 = {10:100,20:200,30:300,40:200}
d2 = {40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)

# Sum of the values in dict
sum = 0
for i in d2.values():
    sum += i

print(f"Sum of value is: {sum}")


# Count frequency of elements in list
l1 = [1,1,1,1,2,2,2,3,3,4,4,4,4,5]
d = {}
for i in l1:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(f"{i} occurrence {d[i]}")