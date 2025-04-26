class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
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
        # Basic email validation
        return "@" in email and "." in email

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance():.2f}"