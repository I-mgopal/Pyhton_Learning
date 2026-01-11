import json
import random
import string
from pathlib import Path


class Bank:
    BASE_DIR = Path(__file__).parent
    DB_FILE = BASE_DIR / "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ---------- File Handling ----------
    def load_data(self):
        if self.DB_FILE.exists():
            try:
                with open(self.DB_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        with open(self.DB_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    # ---------- Utility ----------
    @staticmethod
    def generate_account_no():
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    def find_user(self, acc_no, pin):
        acc_s = str(acc_no).strip()
        pin_s = str(pin).strip()
        return next(
            (
                u
                for u in self.data
                if str(u.get("accountNo", "")).strip() == acc_s
                and str(u.get("pin", "")).strip() == pin_s
            ),
            None,
        )

    # ---------- Core Features ----------
    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be ≥18 and PIN must be 4 digits"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account_no(),
            "balance": 0
        }

        self.data.append(user)
        self.save_data()
        return True, user

    def deposit(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid account or PIN"

        if amount <= 0:
            return False, "Invalid amount"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid account or PIN"

        if amount <= 0 or amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]

    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid account or PIN"

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin and len(str(new_pin)) == 4:
            user["pin"] = new_pin

        self.save_data()
        return True, "Updated successfully"

    def delete_account(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid account or PIN"

        self.data.remove(user)
        self.save_data()
        return True, "Account deleted"
