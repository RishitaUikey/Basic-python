# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print("Account created successfully.")
        else:
            print("Error: Account already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("Deposit successful. Current balance:", self.accounts[account_number])
        else:
            print("Error: Account does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("Withdrawal successful. Current balance:", self.accounts[account_number])
            else:
                print("Error: Insufficient balance.")
        else:
            print("Error: Account does not exist.")

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Error: Account does not exist.")
            return None

bank = Bank()
bank.create_account("123456")
bank.deposit("123456", 1000)
bank.withdraw("123456", 500)

print("Balance in account 123456:", bank.get_balance("123456"))
