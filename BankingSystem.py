import random


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, password, initial_balance):
        accno = random.randint(100000, 900000)
        while accno in self.accounts:
            accno = random.randint(100000, 900000)
        self.accounts[accno] = {
            'name': name,
            'password': password,
            'balance': initial_balance
        }
        return accno

    def login(self, accno, password):
        if accno in self.accounts and self.accounts[accno]['password'] == password:
            return self.accounts[accno]
        else:
            return None

    def deposit(self, accno, amount):
        if accno in self.accounts:
            self.accounts[accno]["balance"] += amount
            print("Deposited $", amount, " New balance: $", self.accounts[accno]["balance"])
            return "Deposit successful"
        else:
            return "Invalid Account Number"

    def withdraw(self, accno, amount):
        if accno in self.accounts:
            if self.accounts[accno]['balance'] >= amount:
                self.accounts[accno]['balance'] -= amount
                print("Withdrawn $", amount, " New balance: $", self.accounts[accno]["balance"])
                return "Withdrawal successful"
            else:
                return 'Insufficient balance.'
        else:
            return 'Invalid account number.'


def main():
    bank = Bank()
    customerlist = [{"accno": 123456, "name": "Rishana", "password": "risha123", "initial_balance": 1000.0},
                    {"accno": 234567, "name": "Sanjana", "password": "sanja12", "initial_balance": 1500.0},
                    {"accno": 345678, "name": "Harsha", "password": "har960", "initial_balance": 2000.0},
                    {"accno": 4567890, "name": "Fathima", "password": "fat963", "initial_balance": 3000.0}]
    for customer in customerlist:
        bank.create_account(customer["name"], customer["password"], customer["initial_balance"])
        bank.accounts[customer["accno"]] = {
            'name': customer["name"],
            'password': customer["password"],
            'balance': customer["initial_balance"]
        }
    print("Welcome to ABC Bank")
    while True:
        print("Banking System Menu:\n1. Create a new account\n2.Login to your existing account\n3.Exit")
        opt = int(input("Please enter your option:"))
        if opt == 1:
            name = input("Enter your name: ")
            password = input("Enter a password: ")
            initial_balance = float(input("Enter initial balance: $"))
            accno = bank.create_account(name, password, initial_balance)
            print("Your account has been created successfully with Account Number:", accno)
        elif opt == 2:
            accno = int(input("Enter your account number: "))
            password = input("Enter your password: ")
            account = bank.login(accno, password)
            if account:
                print("Welcome", account['name'], "!")
                while True:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")

                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        amount = float(input("Enter the amount to deposit: $"))
                        deposit_result = bank.deposit(accno, amount)
                        print(deposit_result)

                    elif choice == 2:
                        amount = float(input("Enter the amount to withdraw: $"))
                        print(bank.withdraw(accno, amount))

                    elif choice == 3:
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid account number. Please try again.")

        elif opt == 3:
            print("Thankyou! Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
