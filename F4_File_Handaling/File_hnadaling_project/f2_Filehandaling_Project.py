from pathlib import Path
import os
def files_in_current_folder():
    print("Updated files are shown at below 👇:")
    current_folder = Path(__file__).parent
    files = [item for item in current_folder.iterdir()
             if item.is_file() and not item.name.startswith('.')]
    for i, file in enumerate(files, 1):
        print(f"{i} : {file.name}")
    print("\n")


def createfile():
    try:
        files_in_current_folder()
        name = input("Enter filename to create: ")
        p =  Path(__file__).parent / name
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file:- ")
                fs.write(data)
        else:
            print("This file already exists")

        print(f"FILE CREATED SUCCESSFULLY")
        files_in_current_folder()

    except Exception as err:
        print(f"An error occured as {err}") 


def readfile():
    try:
        files_in_current_folder()
        name = input("Enter filename to read: ")
        p =  Path(__file__).parent / name
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
        else:
            print("This file doesn't exists")

        print(f"FILE READED SUCCESSFULLY")
        files_in_current_folder()

    except Exception as err:
        print(f"An error occured as {err}") 

def updatefile():
    try:
        files_in_current_folder()
        name = input("Tell which file you want to update:- ")
        p = Path(__file__).parent/name
        if p.exists() and p.is_file():
            print("Choose Option from below")
            print("1. Change the name\n 2. Overrite the data\n 3.Append the data")
            value = int(input("Tell you response:- "))
            match value:
                case 1:
                    name2 = input("Tell your new file name:- ")
                    p2 = Path(__file__).parent/name2
                    p.rename(p2)

                #For over write
                case 2:
                    with open(p,"w") as fs:
                        data = input("What you want to over write in this file:- ")
                        fs.write(data)

                #For append
                case 3:
                    with open(p,"a") as fs:
                        data = input("What you want to over append in this file:- ")
                        fs.write(" "+data)
            print(f"FILE UPDATED SUCCESSFULLY")
    except Exception as err:
        print(f"An error occured as {err}") 

def deletefile():
    try:
        files_in_current_folder()
        name = input("Tell which file you want to delete:- ")
        p = Path(__file__).parent/name
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"FILE DELETED SUCCESSFULLY")
            files_in_current_folder()
        else:
            print("File doesn't exist")
    except Exception as err:
        print(f"An error occured as {err}") 

print("--------------------- Welcome -----------------------------\n")
print("--------------------- Workflow ----------------------------")
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for Updating a file")
print("Press 4 for deletion a file")
check = int(input("Please Enter yout Response:- "))

match check:
    case 1:
        createfile()
    case 2:
        readfile()
    case 3:
        updatefile()
    case 4:
        deletefile()
    case _:
        print("Again Run and Choose the correct option")