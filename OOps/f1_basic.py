class Factory:
    a = 12 #attribute
    def hello(self): #method
        print("This is method")

print(Factory().a)
Factory().hello()