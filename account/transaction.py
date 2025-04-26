from datetime import datetime

class Transaction:
    VALID_TYPES = {"deposit", "withdraw"}

    def __init__(self, amount, transaction_type):
        """
        Initialize a Transaction instance.

        Args:
            amount (float): The amount of the transaction. Must be positive.
            transaction_type (str): Either "deposit" or "withdraw".

        Raises:
            ValueError: If transaction_type is invalid or amount is non-positive.
        """
        if transaction_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid transaction_type '{transaction_type}'. Must be 'deposit' or 'withdraw'.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount:.2f}"

    def __repr__(self):
        return (f"Transaction(amount={self.amount}, "
                f"transaction_type='{self.transaction_type}', "
                f"timestamp={self.timestamp.isoformat()})")

    def to_dict(self):
        """Return a dictionary representation of the transaction."""
        return {
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp.isoformat()
        }
