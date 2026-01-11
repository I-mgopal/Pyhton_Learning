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
    print(database)
    
    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))


    def Createaaccount(self):
        info = {
            "name": input("Tell your name:- "),
            "age": int(input("Tell your age:- ")),
            "email":input("tell your email:- "),
            "pin": int(input("tell your pin:- ")),
            "accountNo":123456,
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

        


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for Deposite money in the bank")
print("Press 3 for withdrawing money the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")


check = int(input("tell your response :- "))

if check==1:
    user.Createaaccount()