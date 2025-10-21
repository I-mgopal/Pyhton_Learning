from pathlib import Path
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def creatfile():
    readfileandfolder()


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for Updating a file")
print("Press 4 for deletion a file")


check = int(input("Please Enter yout Response:- "))

if check==1:
    creatfile()