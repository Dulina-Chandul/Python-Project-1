from account.transaction import Transaction

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Invalid initial balance!")
            initial_balance = 0
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.name = name
        self.email = email

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount is invalid!")
            return False
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))
        return True

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
        if self.balance < amount:
            print("Insufficient Balance!")
            return False
        self.balance -= amount  # Fixed: Now correctly subtracts the amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
        if self.balance - amount < self.MIN_BALANCE:
            print(f"Minimum balance of ${self.MIN_BALANCE} required for Savings Account!")
            return False
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_account_type(self):
        return "Savings account"


class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current account"


class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
        if (self.balance - amount) < 100:
            print("A minimum balance of Rs.100 needed to withdraw from a Students account!")
            return False
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_account_type(self):
        return "Students account"