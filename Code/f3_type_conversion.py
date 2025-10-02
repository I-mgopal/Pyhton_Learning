#Explicit  
#**Convert one Number datatype to another number datatype or string not to other datatype
# Interger to String 
num1 = 12
str1 = str(12)
print(type(str1))
print(str1)


# String to Integer
str2 = '136'
num2 = int(str2)
print(type(num2))
print(num2)
"""But str2='ufuisdjf' and try to convert into int or float ot complex give Error """


# String to Float
num3 = float(str2)
print(type(num3))
print(num3)

# String list
list1 = list(str2)
print(type(list1))
print(list1)


# String to Float
set1 = set(str2)
print(type(set1))
print(set1)


# String to Dic - not possible

# String to Tuple
tup1 = tuple(str2)
print(type(tup1))
print(tup1)
