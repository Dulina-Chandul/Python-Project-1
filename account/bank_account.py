from account.transaction import Transaction

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Invalid initial balance!")
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.name = name
        self.email = email

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount is invalid!")
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))
        return True

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        self.balance -= amount
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
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        if self.balance - amount <= self.MIN_BALANCE:
            raise ValueError(f"Cannot withdraw below minimum balance of ${self.MIN_BALANCE}!")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_account_type(self):
        return "Savings Account"


class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current Account"


class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance - amount < 100:
            raise ValueError("Cannot withdraw below minimum balance of $100!")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_account_type(self):
        return "Students Account"