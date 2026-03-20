class BankAccount:
    def __init__(self, account_number: int = 0, owner_name: str = "", balance: float = 0.0) -> None:
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
class Bank:
    def __init__(self) -> None:
        self.accounts:dict[int, BankAccount] = {}
    def create_account(self) -> None:
        """Create a new bank account and add it to the accounts dictionary."""
        while True:
            try:
                account_number = int(input("Enter account number: "))
                if account_number in self.accounts:
                    print("Account number already exists. Try a different number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for account number.")

        owner_name = input("Enter owner name: ").strip()
        while not owner_name:
            print("Owner name cannot be empty.")
            owner_name = input("Enter owner name: ").strip()

        while True:
            try:
                balance = float(input("Enter initial balance: "))
                if balance < 0:
                    print("Initial balance cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for balance.")

    # Create BankAccount object and add it to the accounts dictionary
        account = BankAccount(account_number, owner_name, balance)
        self.accounts[account_number] = account
        print(f"Account created successfully for {owner_name} with account number {account_number}.")
    def deposit(self, amount: float, account_number: int) -> float:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.accounts[account_number].balance += amount
        return self.accounts[account_number].balance
    def withdraw(self, amount: float, account_number: int) -> float:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.accounts[account_number].balance:
            raise ValueError("Insufficient funds")
        self.accounts[account_number].balance -= amount
        return self.accounts[account_number].balance
    def get_balance(self, account_number: int) -> float:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number].balance
    def find_account(self, account_number: int) -> BankAccount | None:
        if account_number not in self.accounts:
            print("Account not found")
            return None
        return self.accounts.get(account_number)
def main() -> None:
    bank=Bank()
    print("Welcome to the Bank Account System")
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Info")
        print("6. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                try:
                    bank.create_account()
                except ValueError as e:
                    print(e)
            case "2":                    
                try:
                    account_number = int(input("Enter account number: "))
                    amount = float(input("Enter deposit amount: "))
                    new_balance = bank.deposit(amount, account_number)
                    print(f"Deposit successful. New balance: {new_balance}")
                except ValueError as e:
                     print(e)
            case '3':
                    try:
                        account_number = int(input("Enter account number: "))
                        amount = float(input("Enter withdrawal amount: "))
                        new_balance = bank.withdraw(amount, account_number)
                        print(f"Withdrawal successful. New balance: {new_balance}")
                    except ValueError as e:
                        print(e)
            
            
            case "4":
                try:
                    account_number = int(input("Enter account number: "))
                    print(f"Current balance: {bank.get_balance(account_number)}")
                except ValueError as e:
                    print(e)
            case "5":
                try:
                    account_number = int(input("Enter account number: "))
                    info = bank.find_account(account_number)
                    if info:
                        print(f"Account Number: {info.account_number}")
                        print(f"Owner Name: {info.owner_name}")
                        print(f"Balance: {info.balance}")
                except ValueError as e:
                    print(e)
            case "6":
                print("Thank you for using the Bank Account System. Goodbye!")
                break
            case _:
                print("Invalid option. Please choose a valid menu item.")
if __name__ == "__main__":
    main()
