class BankAccount:
    def __init__(self,account_no,owner,balance=0.0):
        self.account_no=account_no
        self.owner=owner
        self._balance=float(balance)
        
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"amount {amount} is deposited to {self.account_no}")
        else:
            print("invalid deposite amount")
    def withdraw(self,amount):
        if 0<amount<=self._balance:
            self._balance-=amount
            print(f"the {amount} is withdraw form our account {self.account_no}")
        else:
            print("infuccient balance or invalid amount")
    def get_balance(self):
        return self._balance
    def account_info(self):
        print(f"Account No: {self.account_no}, Owner: {self.owner}, Balance: {self._balance}")


def bank_operations():
    account=BankAccount("01","Tejas",100000)

    def deposit_case():
        try:
            amount=float(input("Enter the amount to add"))
            account.deposit(amount)
        except:
            print("invalid input!please enter valid number")
            
    def withdraw_case():
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    def check_balance_case():
        print(f"Current balance: {account.get_balance()}")

    def account_info_case():
        account.account_info()

    def exit_case():
        print("Exiting... Thank you for using the Bank System!")
        return False 
    
    switch={
        1:deposit_case,
        2:withdraw_case,
        3:check_balance_case,
        4:account_info_case,
        5:exit_case
    }

    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")
        
        try:
            choice=int(input("Enter your choice:"))
            if choice in switch:
                result = switch[choice]()
                if result is False:
                    break
            else:
                print("invalid choise!please try again")
        except ValueError:
            print("please enter valid number")
            
            
bank_operations()