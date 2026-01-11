import streamlit as st
from backend import Bank  # backend file

bank = Bank()

st.set_page_config(page_title="Bank System", page_icon="🏦")
st.title("🏦 Simple Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Details",
        "Update Details",
        "Delete Account",
    ]
)

# ---------------- CREATE ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")
    if st.button("Create Account"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be 4 digits")
        else:
            success, result = bank.create_account(name, age, email, int(pin))
        if success:
            st.success("Account created successfully!")
            st.json(result)
        else:
            st.error(result)

# ---------------- COMMON AUTH ----------------
def auth():
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    return acc, pin

# ---------------- DEPOSIT ----------------
if menu == "Deposit Money":
    st.subheader("Deposit Money")
    acc, pin = auth()
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc.strip(), pin)
        # deposit requires amount, fix call
        # Bank.deposit expects (acc_no, pin, amount)
        success, msg = bank.deposit(acc.strip(), pin, amount)
        st.success(f"Balance: {msg}") if success else st.error(msg)

# ---------------- WITHDRAW ----------------
if menu == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc, pin = auth()
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc.strip(), pin, amount)
        st.success(f"Balance: {msg}") if success else st.error(msg)

# ---------------- VIEW ----------------
if menu == "View Details":
    st.subheader("Account Details")
    acc, pin = auth()

    if st.button("Show"):
        user = bank.find_user(acc.strip(), pin)
        st.json(user) if user else st.error("Invalid credentials")

# ---------------- UPDATE ----------------
if menu == "Update Details":
    st.subheader("Update Account")
    acc, pin = auth()

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        success, msg = bank.update_details(
            acc.strip(),
            pin,
            name=name or None,
            email=email or None,
            new_pin=int(new_pin) if new_pin else None,
        )
        st.success(msg) if success else st.error(msg)

# ---------------- DELETE ----------------
if menu == "Delete Account":
    st.subheader("Delete Account")
    acc, pin = auth()

    if st.button("Delete"):
        success, msg = bank.delete_account(acc.strip(), pin)
        st.success(msg) if success else st.error(msg)
