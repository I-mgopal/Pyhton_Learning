#Q16 Return GCD and LCM
def GCD(a,b):
    while b:
        a, b = b, a%b
    return a
    
#Q17 LCM
def LCM(a,b):
    lcm = int((a*b)/GCD(a,b))
    return lcm

print(f"GCD is {GCD(6,2)}")
print(f"LCM is {LCM(6,2)}")

