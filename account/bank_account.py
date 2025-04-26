from account.transaction import Transaction

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        """
        Initialize a generic bank account.
        
        Args:
            name (str): Account holder's name.
            email (str): Account holder's email.
            initial_balance (float): Starting balance (non-negative).
        
        Raises:
            ValueError: If initial_balance is negative or not a number.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Invalid initial balance!")
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.name = name
        self.email = email

    def deposit(self, amount):
        """
        Deposit amount into account.
        
        Args:
            amount (float): Amount to deposit (positive).
        
        Raises:
            ValueError: If amount is not positive.
        
        Returns:
            bool: True if deposit successful.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount is invalid!")
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))
        return True

    def withdraw(self, amount):
        """
        Withdraw amount from account.
        
        Args:
            amount (float): Amount to withdraw (positive).
        
        Raises:
            ValueError: If amount is invalid or insufficient balance.
        
        Returns:
            bool: True if withdrawal successful.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def get_transaction_history(self):
        """Return list of all transactions."""
        return self.transactions_history

    def get_account_type(self):
        """Return account type string."""
        return self.account_type

    def __str__(self):
        return f"{self.account_type} - {self.name}: Balance ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        if self.balance - amount < self.MIN_BALANCE:
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
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount is invalid!")
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Cannot withdraw below minimum balance of ${self.MIN_BALANCE}!")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_account_type(self):
        return "Student Account"
