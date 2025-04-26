from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
from account.user import User
from account.transaction import Transaction

console = Console()
users = []

def create_user():
    """Create a new user and add them to the system"""
    console.print("\n[bold cyan]Create New User[/bold cyan]")
    name = Prompt.ask("Enter user name")
    email = Prompt.ask("Enter user email")
    
    try:
        new_user = User(name, email)
        for user in users:
            if user.email == email:
                console.print("User with this email already exists!", style="bold red")
                Prompt.ask("\nPress Enter to continue")
                return
        users.append(new_user)
        console.print(f"User [bold green]{name}[/bold green] created successfully!", style="bold green")
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
    Prompt.ask("\nPress Enter to continue")

def list_users():
    """Display all users in the system"""
    console.print("\n[bold cyan]User List[/bold cyan]")
    
    if not users:
        console.print("No users available in the system.", style="yellow")
        Prompt.ask("\nPress Enter to continue")
        return
    
    table = Table(title="👤 Users")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Email", style="blue")
    table.add_column("Accounts", style="magenta", justify="center")
    
    for i, user in enumerate(users):
        table.add_row(
            str(i + 1),
            user.name,
            user.email,
            str(user.get_account_count())
        )
    
    console.print(table)
    Prompt.ask("\nPress Enter to continue")
# ... (previous imports and code)

def create_account():
    """Create a new account for an existing user"""
    console.print("\n[bold cyan]Create New Account[/bold cyan]")
    
    if not users:
        console.print("[bold red]No users available. Please create a user first.[/bold red]")
        Prompt.ask("\nPress Enter to continue")
        return
    
    try:
        user = select_user()
    except ValueError as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        Prompt.ask("\nPress Enter to continue")
        return
    
    # ... (rest of account type selection code remains same)
    
    try:
        if account_choice == "1":
            account = SavingsAccount(user.name, user.email, initial_balance)
        elif account_choice == "2":
            account = CurrentAccount(user.name, user.email, initial_balance)
        elif account_choice == "3":
            account = StudentAccount(user.name, user.email, initial_balance)
        else:
            console.print("[bold red]Invalid account type![/bold red]")
            Prompt.ask("\nPress Enter to continue")
            return
        # ... (rest of account creation code)

def select_user():
    """Helper function to select a user from the list"""
    if not users:
        raise ValueError("No users available. Please create a user first.")
    
    # ... (table setup code remains same)
    
    try:
        max_id = len(users)
        choice = Prompt.ask(f"Select user by ID (1-{max_id})")
        choice = int(choice)
        if choice < 1 or choice > len(users):
            raise ValueError(f"[bold red]Invalid user ID. Please select 1-{len(users)}[/bold red]")
        return users[choice - 1]
    except ValueError:
        raise ValueError("[bold red]Invalid user selection.[/bold red]")

# ... (rest of file remains same)

def select_account(user):
    """Helper function to select an account from a user"""
    if not user.accounts:
        console.print(f"User {user.name} has no accounts.", style="yellow")
        return None
    
    table = Table(title=f"💰 {user.name}'s Accounts")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Account Type", style="green")
    table.add_column("Balance", style="blue", justify="right")
    
    for i, account in enumerate(user.accounts):
        table.add_row(
            str(i + 1),
            account.get_account_type(),
            f"${account.get_balance():.2f}"
        )
    
    console.print(table)
    
    try:
        choice = int(Prompt.ask("Select account by ID", default="1"))
        if choice < 1 or choice > len(user.accounts):
            console.print("Invalid account selection.", style="bold red")
            return None
        return user.accounts[choice - 1]
    except ValueError:
        console.print("Invalid account selection.", style="bold red")
        return None

def deposit_money():
    """Deposit money into a user's account"""
    console.print("\n[bold cyan]Deposit Money[/bold cyan]")
    
    try:
        user = select_user()
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
        Prompt.ask("\nPress Enter to continue")
        return
    
    account = select_account(user)
    if not account:
        Prompt.ask("\nPress Enter to continue")
        return
    
    try:
        amount = float(Prompt.ask("Enter deposit amount"))
        if amount <= 0:
            console.print("Deposit amount must be positive!", style="bold red")
            Prompt.ask("\nPress Enter to continue")
            return
    except ValueError:
        console.print("Invalid amount entered!", style="bold red")
        Prompt.ask("\nPress Enter to continue")
        return
    
    try:
        old_balance = account.get_balance()
        account.deposit(amount)
        new_balance = account.get_balance()
        console.print(f"[bold green]Successfully deposited ${amount:.2f}![/bold green]")
        console.print(f"Previous balance: ${old_balance:.2f}")
        console.print(f"New balance: ${new_balance:.2f}")
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
    Prompt.ask("\nPress Enter to continue")

def withdraw_money():
    """Withdraw money from a user's account"""
    console.print("\n[bold cyan]Withdraw Money[/bold cyan]")
    
    try:
        user = select_user()
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
        Prompt.ask("\nPress Enter to continue")
        return
    
    account = select_account(user)
    if not account:
        Prompt.ask("\nPress Enter to continue")
        return
    
    try:
        amount = float(Prompt.ask("Enter withdrawal amount"))
        if amount <= 0:
            console.print("Withdrawal amount must be positive!", style="bold red")
            Prompt.ask("\nPress Enter to continue")
            return
    except ValueError:
        console.print("Invalid amount entered!", style="bold red")
        Prompt.ask("\nPress Enter to continue")
        return
    
    try:
        old_balance = account.get_balance()
        account.withdraw(amount)
        new_balance = account.get_balance()
        console.print(f"[bold green]Successfully withdrew ${amount:.2f}![/bold green]")
        console.print(f"Previous balance: ${old_balance:.2f}")
        console.print(f"New balance: ${new_balance:.2f}")
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
    Prompt.ask("\nPress Enter to continue")

def view_transactions():
    """View transaction history for a user's account"""
    console.print("\n[bold cyan]View Transactions[/bold cyan]")
    
    try:
        user = select_user()
    except ValueError as e:
        console.print(f"Error: {str(e)}", style="bold red")
        Prompt.ask("\nPress Enter to continue")
        return
    
    account = select_account(user)
    if not account:
        Prompt.ask("\nPress Enter to continue")
        return
    
    transactions = account.get_transaction_history()
    if not transactions:
        console.print("No transactions found for this account.", style="yellow")
        Prompt.ask("\nPress Enter to continue")
        return
    
    table = Table(title=f"📜 Transaction History - {account.get_account_type()}")
    table.add_column("Date & Time", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Amount", style="blue", justify="right")
    
    for transaction in transactions:
        transaction_type = transaction.transaction_type.upper()
        style = "green" if transaction_type == "DEPOSIT" else "red"
        amount_str = f"${transaction.amount:.2f}"
        
        table.add_row(
            transaction.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            f"[{style}]{transaction_type}[/{style}]",
            amount_str
        )
    
    console.print(table)
    console.print(f"Current Balance: ${account.get_balance():.2f}")
    Prompt.ask("\nPress Enter to continue")