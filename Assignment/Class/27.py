''' Write a  Python class BankAccount with attributes like account_number, balance, date_of_opening 
and customer_name, and methods like deposit, withdraw, and check_balance.'''

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")

account = BankAccount("1234567890", "John Doe", 1000, "2024-04-20")
account.deposit(500)
account.withdraw(200)
account.check_balance()
