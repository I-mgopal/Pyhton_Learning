class Factory:
    a = 12
    def hello(self):
        print("Hello how are you")
    print("Outside of the hello class")

obj = Factory()
obj1 = Factory()
obj2 = Factory()
print(obj.a)
obj.hello()