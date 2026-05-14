# Represents a bank account
class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        # Ensure deposit amount is positive
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        # Check for positive amount and sufficient funds
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    def add_interest(self, rate=0.02):
        # Add interest to the balance (default is 2%)
        interest_amount = self.balance * rate
        self.balance += interest_amount
        print(f"Interest of ${interest_amount:.2f} added to the account.")

    def get_balance(self):
        return self.balance


# Manages the user menu
class Menu:
    def __init__(self):
        """Sets up the initial menu options."""
        self.options = [
            "Open a new account",
            "Deposit money into your account",
            "Withdraw money from your account",
            "Add interest to your account",
            "Get the current balance of your account",
            "Quit"
        ]

    def add_option(self, option_text):
        """Lets you add a new option to the menu."""
        self.options.append(option_text)

    def get_input(self):
        """Shows menu, then gets and validates user's numerical choice."""
        print("\n===Bank Menu===")
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

        while True: # Keep asking until valid input
            try:
                choice_str = input(f"Choose an option (1-{len(self.options)}): ")
                choice = int(choice_str)
                if 1 <= choice <= len(self.options):
                    return choice # Got a valid choice
                else:
                    print(f"Invalid choice. Please select a number between 1 and {len(self.options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Main Program
menu = Menu()
account = None  # No bank account exists at the start

while True:
    user_choice = menu.get_input()

    if user_choice == 1:
        # 1. Open new account
        account = BankAccount()
        print("New account created successfully.")

    elif user_choice == 2:
        # 2. Deposit
        if account:
            try:
                deposit_amount_str = input("Enter amount to deposit: ")
                deposit_amount = float(deposit_amount_str)
                account.deposit(deposit_amount)
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
        else:
            print("No account found. Please open an account first (option 1).")

    elif user_choice == 3:
        # 3. Withdraw
        if account:
            try:
                withdraw_amount_str = input("Enter amount to withdraw: ")
                withdraw_amount = float(withdraw_amount_str)
                account.withdraw(withdraw_amount)
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
        else:
            print("No account found. Please open an account first (option 1).")

    elif user_choice == 4:
        # 4. Add interest
        if account:
            account.add_interest()
        else:
            print("No account found. Please open an account first (option 1).")

    elif user_choice == 5:
        # 5. Get balance
        if account:
            print(f"Current balance: ${account.get_balance():.2f}")
        else:
            print("No account found. Please open an account first (option 1).")

    elif user_choice == 6:
        # 6. Quit
        print("Goodbye!")
        break