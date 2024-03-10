class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, password, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'password': password, 'balance': initial_balance}
            print(f"Account created successfully for account number {account_number}")
        else:
            print("Account already exists. Please choose a different account number.")

    def login(self, account_number, password):
        if account_number in self.accounts and self.accounts[account_number]['password'] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid account number or password. Please try again.")
            return False

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Amount deposited successfully. New balance: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number. Please check and try again.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Amount withdrawn successfully. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance. Please check your account balance.")
        else:
            print("Invalid account number. Please check and try again.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account Balance: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number. Please check and try again.")



bank = BankSystem()


bank.create_account("123456", "password123", 1000)


if bank.login("123456", "password123"):
   
    bank.deposit("123456", 500)

   
    bank.withdraw("123456", 200)

   
    bank.check_balance("123456")
