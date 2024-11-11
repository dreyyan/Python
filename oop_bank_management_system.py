# Bank Management System

class Bank:
    account_count = 0
    # Constructor
    def __init__(self, account_number, account_holder, account_balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance
        Bank.account_count += 1

    # Display Info
    def DisplayInfo(self):
        print(f'Account #{self.account_count}')
        print("------------------------")
        print(f'Acc. No.: {self.account_number}')
        print(f'Acc. Holder.: {self.account_holder}')
        print(f'Balance.: ${self.account_balance}')
        print("------------------------|")

    # Deposit
    def Deposit(self):
        print("depositing amount...")
        deposit_amount = int(input("Enter amount: $"))

        while deposit_amount < 0:
            print("ERROR | invalid_deposit_amount")
            deposit_amount = int(input("Enter amount: $"))

        self.account_balance += deposit_amount
        print(f'successfully deposited ${deposit_amount} | [#{self.account_number}]')
        print(f'>> Current Balance: ${self.account_balance}')
        print("-------------------------------------|")

    # Withdraw
    def Withdraw(self):
        print("withdrawing amount...")
        print(f'Current Balance: ${self.account_balance}')
        withdrawal_amount = int(input("Enter amount: $"))

        while withdrawal_amount > self.account_balance:
            print("ERROR | invalid_withdrawal_amount")
            withdrawal_amount = int(input("Enter amount: $"))

        self.account_balance -= withdrawal_amount
        print(f'>> successfully withdrawn ${withdrawal_amount} | [#{self.account_number}]')
        print(f'>> Current Balance: ${self.account_balance}')
        print("-------------------------------------|")

acc1 = Bank("001", "Adrian Tan")
acc1.DisplayInfo()
acc1.Deposit()
acc1.Withdraw()