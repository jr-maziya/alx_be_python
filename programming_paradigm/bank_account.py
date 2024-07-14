class BankAccount():
    
    def __init__(self, account_balance):
        self.user_account_balance = account_balance

    def deposit(self, amount):
        self.user_account_balance =+ amount

    def withdraw(self, amount):
        amount = float(amount)
        if self.user_account_balance > amount:
            self.user_account_balance =- amount
        else:
            False
    
    def display_balance(self):
         print(f"Account balance is {self.user_account_balance}")

# account = BankAccount()
# account.deposit(500)
# account.display_balance()
