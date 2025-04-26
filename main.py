import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

from bank_operator.bank_operator import create_user, list_users, create_account, deposit_money, withdraw_money, view_transactions

console = Console()

def menu():
    """Display the main menu and handle user input"""
    try:
        while True:
            console.clear()
            # Display welcome banner
            console.print(Panel.fit(
                "[bold magenta]Welcome to PyBank CLI[/bold magenta]\n"
                "[italic]A Python-based Banking System[/italic]",
                border_style="green"
            ))
            
            # Create menu table
            table = Table(title="🏦 Bank System Menu", title_style="bold magenta")
            table.add_column("Option", style="cyan", justify="center")
            table.add_column("Description", style="white")
            table.add_row("1", "Create User")
            table.add_row("2", "List Users")
            table.add_row("3", "Add Account")
            table.add_row("4", "Deposit")
            table.add_row("5", "Withdraw")
            table.add_row("6", "View Transactions")
            table.add_row("7", "Exit")
            console.print(table)
            
            # Get user choice with validation
            choice = Prompt.ask(
                "👉 Choose option", 
                choices=[str(i) for i in range(1, 8)], 
                default="7"
            )
            
            # Process the chosen option
            if choice == '1':
                create_user()
            elif choice == '2':
                list_users()
            elif choice == '3':
                create_account()
            elif choice == '4':
                deposit_money()
            elif choice == '5':
                withdraw_money()
            elif choice == '6':
                view_transactions()
            elif choice == '7':
                console.print("\n👋 Exiting... Thank you for using the PyBank System!", style="bold green")
                break
    except KeyboardInterrupt:
        console.print("\n\n⚠️ Program interrupted. Exiting safely...", style="bold yellow")
    except Exception as e:
        console.print(f"\n\n❌ An unexpected error occurred: {str(e)}", style="bold red")
        console.print("Please restart the application.", style="bold red")

if __name__ == "__main__":
    console.print("[bold cyan]Starting PyBank CLI...[/bold cyan]")
    menu()