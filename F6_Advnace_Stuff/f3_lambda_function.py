addition = lambda a,b : a+b
print(addition(12,13))

even_odd = lambda num:"Even" if num%2==0 else "Odd"
print(even_odd(12))


#double the number
a = [1,2,3,4]
# def double(x):
#     return x*2
# result = map(double, a)
result = map(lambda x:x*2 , a)
print(list(result))


#Evens using filter
num = [1,3,5,2,6,8,20]
# evens = filter(lambda x: x%2==0, num)
evens = filter(lambda x: True if x%2==0 else False, num)
print(list(evens))
