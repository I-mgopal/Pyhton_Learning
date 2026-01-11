import json
import random
import string
from pathlib import Path

class Bank:
    BASE_DIR = Path(__file__).parent
    database = BASE_DIR/ "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.load(fs)
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    
    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k= 3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id) # Convert list to string


    def Createaaccount(self):
        info = {
            "name": input("Tell your name:- "),
            "age": int(input("Tell your age:- ")),
            "email":input("tell your email:- "),
            "pin": int(input("tell your pin:- ")),
            "accountNo":Bank.__accountgenerate(),
            "balance":0
        }

        #Checking
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you can't create the account")
        else:
            print("\nAccount has been created sucesfully: ")
            for i in info:
                print(f"{i} - {info[i]}")
            print("Please note down your account number")
            Bank.data.append(info)
            Bank.update()
    
    def Depositemoney(self):
        accountnum = input("Give your account number: ")
        pinnum = int(input("Give your account number: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accountnum and i['pin'] == pinnum]

        if not userdata:
            print("Sorry no data found!")
        else:
            amount = int(input("Enter the deposite amount: "))
            userdata[0]['balance']+=amount
            Bank.update()
            print("Amount deposited sucessfully!")

    def Withdramoney(self):
        accountnum = input("Give your account number: ")
        pinnum = int(input("Give your account number: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accountnum and i['pin'] == pinnum]

        if not userdata:
            print("Sorry no data found!")
        else:
            amount = int(input("Enter the withdraw amount: "))
            userdata[0]['balance']-=amount
            Bank.update()
            print("Amount withdrew sucessfully!")
    
    def Showdetails(self):
        accountnum = input("Give your account number: ")
        pinnum = int(input("Give your account number: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accountnum and i['pin'] == pinnum]     

        if not userdata:
            print("Sorry no data found!")
        else:
            print("-" * 42)
            for i,j in userdata[0].items():
                print(f"| {i:<10} | {j:<25} |")
            print("-" * 42)

    def Updatedetails(self):
        accountnum = input("Give your account number: ")
        pinnum = int(input("Give your account number: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accountnum and i['pin'] == pinnum] 
        print(userdata)

        if not userdata:
            print("Sorry no data found!")
        else:
            print("You can't chnage the age, account no, balance")
            print("Fill the details for chnage or leave it empty if no chnage")

            newdata = {
                "name": input("Please tell new name or Enter: "),
                "email": input("Enter new email or Enter blank: "),
                "pin": int(input("Enter new pin or Enter blank: "))
            }

            if newdata["name"].strip() and newdata["name"] != userdata[0]["name"]:
                userdata[0]["name"] = newdata["name"]
            if newdata["email"].strip() and newdata["email"] != userdata[0]["email"]:
                userdata[0]["email"] = newdata["email"]
            if newdata["pin"] != userdata[0]["pin"]:
                userdata[0]["pin"] = newdata["pin"]
            Bank.update()
            print("Update Sucessfull!")
    
    def Deleteuser(self):
        accountnum = input("Give your account number: ")
        pinnum = int(input("Give your account number: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accountnum and i['pin'] == pinnum] 

        if not userdata:
            print("Sorry no data found!")
        else:
            check = input("For further processing Enter: Y or N")
            if check=='N':
                print("Terminate the deletion")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.update()
                print("Acoount deleted SuccessFully!")




        


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for Deposite money in the bank")
print("Press 3 for withdrawing money the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")


check = int(input("tell your response :- "))



match check:
    case 1:
        user.Createaaccount()
    case 2:
        user.Depositemoney()
    case 3:
        user.Withdramoney()
    case 4:
        user.Showdetails()
    case 5:
        user.Updatedetails()
    case 6:
        user.Deleteuser()
    case _:
        print("Choose a valid number")