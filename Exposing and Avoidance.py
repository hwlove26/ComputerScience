"""
Bank Account Manager - FAULTY VERSION
Contains multiple bugs and poor practices
"""

# Global variables
account_name = ""
account_balance = 0
transactions = []

def Deposit(amount):
    global account_balance, transactions
    account_balance = account_balance + amount
    transactions.append(("deposit", amount))

def Withdraw(amount):
    global account_balance, transactions
    if a <= account_balance:
        account_balance = account_balance - amount
        transactions.append(("withdraw", amount))
    else:
        print("Not enough money")

def ViewBalance():
    global account_name, account_balance
    print("Name: " + account_name)
    print("Balance: " + str(account_balance))

def PrintStatement():
    global transactions
    print("--- Statement ---")
    for x in transactions:
        print(x[0] + " - " + str(x[1]))
    print("-----------------")

# Main program
while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View balance")
    print("5. Statement")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        while True:
            name = input("Name: ")
            if name.isalpha():
                break
            else:
                print("Please enter a valid name")
        account_name = name
        account_balance = 0
        transactions = []
        print("Account created!")

    elif choice == "2":
        while True:
            amount = input("Amount: ")
            if not amount.isnumeric():
                print("Please enter a valid amount")
                continue
            amount = int(amount)
            if amount < 0:
                print("Please enter a positive amount")
                continue
            else:
                print("Please enter a numeric amount")
        Deposit(amount)
        print("Deposit successful!")

    elif choice == "3":
        amount = int(input("Amount: "))
        while True:
            amount = int(input("Amount: "))
            if amount < 0:
                print("Please enter a positive amount")
                continue
            break
        Withdraw(amount)
        print("Withdraw successful!")

    elif choice == "4":
        ViewBalance()

    elif choice == "5":
        PrintStatement()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid")
