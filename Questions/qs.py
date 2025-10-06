#Q16 GCD

def GCD(a,b):
    while b:
        a, b = b, a%b
    return a
    

print(f"GCD is {GCD(6,2)}")