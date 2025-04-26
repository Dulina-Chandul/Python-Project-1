import re
from account.bank_account import BankAccount

class User:
    def __init__(self, name, email):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format!")
        self._name = name
        self._email = email
        self.accounts = []

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def add_account(self, account):
        """
        Adds a BankAccount instance to the user's account list.

        Args:
            account (BankAccount): The bank account to add.

        Raises:
            ValueError: If the account is not a BankAccount instance.

        Returns:
            bool: True if the account was added successfully.
        """
        if not isinstance(account, BankAccount):
            raise ValueError("Invalid account type! Must be a BankAccount instance.")
        self.accounts.append(account)
        return True

    def get_total_balance(self):
        """Returns the total balance across all user accounts."""
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        """Returns the number of accounts the user has."""
        return len(self.accounts)

    def remove_account(self, account):
        """
        Removes an account from the user's account list if it exists.

        Args:
            account (BankAccount): The bank account to remove.

        Returns:
            bool: True if the account was removed, False otherwise.
        """
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False

    def is_valid_email(self, email):
        """Validates the email format using regex."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance():.2f}"

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r}, accounts={self.accounts!r})"
