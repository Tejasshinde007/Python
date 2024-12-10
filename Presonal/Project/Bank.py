import os

class BankAccount:
    def __init__(self, account_no, holder_name, balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdraw", amount)
        else:
            print("Insufficient Balance")

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
        }
        self.transaction_history.append(transaction)
        self.save_transaction_history()

    def save_transaction_history(self):
        if not self.transaction_history:
            return  

        with open(f"{self.account_no}_transactions.txt", 'a') as file:
            for t in self.transaction_history:
                file.write(f"{t['type']} - {t['amount']} | Balance: {t['balance']}\n")

        

    def load_transaction_history(self):
        if os.path.exists(f"{self.account_no}_transactions.txt"):
            print(f"Loading transaction history for account {self.account_no}:")
            with open(f"{self.account_no}_transactions.txt", 'r') as file:
                for line in file:
                    print(line.strip())
        else:
            print("No transaction history found.")

    @staticmethod
    def load_accounts():
        accounts = [
            BankAccount('123456', 'Tejas Shinde', 10000),
            BankAccount('654321', 'Ashu Rohom', 50000),
            BankAccount('654321', 'Tejas Nalge', 25000),
            BankAccount('654321', 'Pratik tambe', 75000)
        ]
        return accounts

def main():
    accounts = BankAccount.load_accounts()

    print("Choose an account:")
    for i, account in enumerate(accounts, start=1):
        print(f"{i}. {account.holder_name} (Account Number: {account.account_no})")

    choice = int(input("Select an account: "))
    selected_account = accounts[choice - 1]

    print(f"\nWelcome, {selected_account.holder_name}!")

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == '1':
            amount = float(input("Enter amount to deposit: "))
            selected_account.deposit(amount)
        elif option == '2':
            amount = float(input("Enter amount to withdraw: "))
            selected_account.withdraw(amount)
        elif option == '3':
            selected_account.load_transaction_history()
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
