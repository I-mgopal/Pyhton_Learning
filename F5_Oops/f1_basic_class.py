class Code:
    a = 12
    def hello(self):
        print("Hello World!")
    print("Outside of the hello class")

# Call the classes
print(Code().a)
Code().hello()