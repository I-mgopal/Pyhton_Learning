def decorate(func): # decorater only capture function
    def wrapper(): # Wrapper Capture the argument
        print("Hi, Hello!")
        func()
    return wrapper

@decorate
def hello():
    print("How are you?")

hello()
print("---------------------Next-------------------------\n")

def decr(addf):
    def wrapper(*args,**kwargs):
        print("HI, there your query is processing")
        # print(args)
        # print(kwargs)
        addf(*args,**kwargs)
        print("Thanks, hope you get right answer")
    return wrapper

@decr
def sum1(a,b,c):
    print(f"Your sum is {a+b+c}")

sum1(20,30,50)
print("---------------------Next-------------------------\n")


#*arge
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"Sum is {sum}\n")

add(1,2,6,245,356,354)


#**kwargs
def info(**kwargs):
    print("Here is the information: ")
    for i in kwargs:
        print(f"{i} - {kwargs[i]}")


info(name="John", age=22, designation="Fortend-AI")