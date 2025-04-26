import re
from account.bank_account import BankAccount

class User:
    def __init__(self, name, email):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format!")
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        if not isinstance(account, BankAccount):
            raise ValueError("Invalid account type! Must be a BankAccount instance.")
        self.accounts.append(account)
        return True

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        return total

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False

    def is_valid_email(self, email):
        # Robust email validation using regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance():.2f}"