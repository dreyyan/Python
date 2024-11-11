# Bank Management System

class Bank:
    account_count = 0
    # Constructor
    def __init__(self, account_number, account_holder, account_balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance
        Bank.account_count += 1

    # [1] | Create Account
    def CreateAccount(self):
        print("creating account...")


    # [2] | Deposit Funds
    def DepositFunds(self):
        print("depositing funds...")

    # [3] | Withdraw Funds
    def WithdrawFunds(self):
        print("withdrawing funds...")

    # [4] | View Account Details
    def ViewAccountDetails(self):
        print("viewing account details...")

    # [5] | Update Account Information
    def UpdateAccountInformation(self):
        print("updating account information...")

    # [6] | Close Account
    def CloseAccount(self):
        print("closing account...")

    # [7] | Transaction History
    def TransactionHistory(self):
        print("viewing transaction history...")

    # [8] | Exit
    def Exit(self):
        print("exiting system...")
        exit()

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

    # Display Bank Menu
    def DisplayMenu(self):
        print("===+==+==+== iBMS ==+==+==+===")
        print("| -Bank-Management-System- |")
        print("-_-_-_-_-_-[BANK]-_-_-_-_-_-")
        print("-------------------------------")
        print("[1] | Create Account")
        print("[2] | Deposit Funds")
        print("[3] | Withdraw Funds")
        print("[4] | View Account Details")
        print("[5] | Update Account Information")
        print("[6] | Close Account")
        print("[7] | Transaction History")
        print("[8] | Exit")
        print("-------------------------------")

        # Exception Handling
        try:
            choice = int(input(">> "))
            if choice < 0 or choice > 8:
                print("ERROR | out_of_bounds_input")

        except ValueError:
            print("ERROR | invalid_input")

        else:
            input_choice = {
                1: CreateAccount,
                2: DepositFunds,
                3: WithdrawFunds,
                4: ViewAccountDetails,
                5: UpdateAccountInformation,
                6: CloseAccount,
                7: TransactionHistory,
                8: Exit
            }

default = Bank("", "")
default.DisplayMenu()
