class Bank:
    account_credentials = {}
    account_list = {}
    account_count = -1
    # Constructor
    def __init__(self, account_number, account_holder, account_balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance
        Bank.account_count += 1

    # Return to Menu
    def return_to_menu(self):
        valid_choices = {'y': self.BankMenu, 'n': self.Exit}
        valid_choice = False
        while not valid_choice:
            choice = input("Return to menu?[y/n]: ")
            if choice not in valid_choices:
                print("ERROR | invalid_input")
            else:
                valid_choice = True
        valid_choices[choice]()

    # [1] | Create Account
    def CreateAccount(self):
        print("creating account...")
        valid_account_number = False
        Bank.account_count += 1
        self.account_number = Bank.account_count
        self.account_holder = input("Account Holder: ")
        print("\naccount created successfully!")
        Bank.ViewAccountDetails(self)
        Bank.account_list[self.account_number] = {
            "account_holder": self.account_holder,
            "account_balance": self.account_balance
        }
        self.return_to_menu()

    # [2] | Deposit Funds
    def Deposit(self):
        valid_account_number = False
        print("depositing funds...")

        while not valid_account_number:
            input_account_number = input("Account No.: ")
            if input_account_number not in Bank.account_list:
                print("ERROR | account_number_not_registered")
            else:
                valid_account_number, valid_deposit_amount = True, False
                while not valid_deposit_amount:
                    try:
                        deposit_amount = int(input("Enter deposit amount: $"))
                        if deposit_amount < 0:
                            print("ERROR | invalid_deposit_amount")
                        else:
                            valid_deposit_amount = True
                    except ValueError:
                        print("ERROR | invalid_amount")

        Bank.account_list[input_account_number]["account_balance"] += deposit_amount
        updated_balance = Bank.account_list[input_account_number]["account_balance"]

        print(f'successfully deposited ${deposit_amount} | [#{input_account_number}]')
        print(f'>> Current Balance: ${updated_balance}')
        print("-------------------------------------|")
        self.return_to_menu()

    # [3] | Withdraw Funds
    def Withdraw(self):
        valid_account_number = False
        print("withdrawing funds...")

        while not valid_account_number:
            input_account_number = input("Account No.: ")
            if input_account_number not in Bank.account_list:
                print("ERROR | account_number_not_registered")
            else:
                valid_account_number, valid_withdrawal_amount = True, False
                while not valid_withdrawal_amount:
                    try:
                        withdrawal_amount = int(input("Enter withdrawal amount: $"))
                        if withdrawal_amount < 0 or withdrawal_amount > Bank.account_list[input_account_number]["account_balance"]:
                            print("ERROR | invalid_withdrawal_amount")
                        else:
                            valid_withdrawal_amount = True
                    except ValueError:
                        print("ERROR | invalid_amount")

        Bank.account_list[input_account_number]["account_balance"] -= withdrawal_amount
        updated_balance = Bank.account_list[input_account_number]["account_balance"]

        print(f'successfully withdrawn ${withdrawal_amount} | [#{input_account_number}]')
        print(f'>> Current Balance: ${updated_balance}')
        print("-------------------------------------|")
        self.return_to_menu()

    # [4] | View Account Details
    def ViewAccountDetails(self):
        print("viewing account details...")
        print("------------------------")
        print(f'Account No.: {self.account_number}')
        print(f'Account Holder: {self.account_holder}')
        print(f'Balance: ${self.account_balance}')
        print("------------------------")
        self.return_to_menu()

    # [5] | Update Account Information
    def UpdateAccountInformation(self):
        print("updating account information...")
        self.return_to_menu()

    # [6] | Close Account
    def CloseAccount(self):
        print("closing account...")
        self.return_to_menu()

    # [7] | Transaction History
    def TransactionHistory(self):
        print("viewing transaction history...")
        self.return_to_menu()

    # [8] | Exit
    def Exit(self):
        print("exiting system...")
        exit()

    def Menu(self):
        print("===+==+==+== iBMS ==+==+==+===")
        print("| -Bank-Management-System- |")
        print("-_-_-_-_-_-[LOGIN]-_-_-_-_-_-")
        print("-------------------------------")
        print("[1] | Login")
        print("[2] | Register")
        print("[3] | Exit")
        print("-------------------------------")

        valid_choice = False
        # Exception Handling
        try:
            while not valid_choice:
                choice = int(input(">> "))
                if choice > 0 and choice < 4:
                    if choice == 1:
                        valid_choice = True
                        self.LoginMenu()
                    elif choice == 2:
                        valid_choice = True
                        self.RegisterMenu()
                    elif choice == 3:
                        valid_choice = True
                        self.Exit()
                    else:
                        valid_choice = False
                        print("ERROR | invalid_input")

        except ValueError:
            print("ERROR | invalid_input")

    # Register User Credentials
    def RegisterMenu(self):
        valid_username, valid_password = False, False
        print("===+==+==+== iBMS ==+==+==+===")
        print("| -Bank-Management-System- |")
        print("-_-_-_-_-[REGISTER]-_-_-_-_-")
        print("-------------------------------")

        while not valid_username:
            username = input("Username: ")
            if len(username) < 3:
                print("ERROR | invalid_username")
            else:
                valid_username = True

        while not valid_password:
            password = input("Password: ")
            if len(password) < 3:
                print("ERROR | invalid_password")
            else:
                valid_password = True

        Bank.account_credentials[username] = password # Add Username & Password to Dict

        print("Proceed to Login Page?")
        print("-----------")
        print("[1] | Yes")
        print("[2] | No")
        print("-----------")

        # Exception Handling
        try:
            choice = int(input(">> "))
            if choice > 0 and choice < 3:
                if choice == 1:
                    self.LoginMenu()
                elif choice == 2:
                    self.Menu()
                else:
                    print("ERROR | invalid_input")
            else:
                print("ERROR | out_of_bounds_input")

        except ValueError:
            print("ERROR | invalid_input")

    # Login User Credentials
    def LoginMenu(self):
        valid_username, valid_password = False, False
        print("===+==+==+== iBMS ==+==+==+===")
        print("| -Bank-Management-System- |")
        print("-_-_-_-_-_-[LOGIN]-_-_-_-_-_-")
        print("-------------------------------")

        while not valid_username:
            username = input("Username: ")
            if username not in Bank.account_credentials:
                print("ERROR | invalid_username")
            else:
                valid_username = True

        while not valid_password:
            password = input("Password: ")
            if Bank.account_credentials[username] != password:
                print("ERROR | invalid_password")
            else:
                valid_password = True

        print("Login Successful!")
        self.BankMenu()

    # Display Bank Menu
    def BankMenu(self):
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

        # Function Library
        input_choice = {
            1: self.CreateAccount,
            2: self.Deposit,
            3: self.Withdraw,
            4: self.ViewAccountDetails,
            5: self.UpdateAccountInformation,
            6: self.CloseAccount,
            7: self.TransactionHistory,
            8: self.Exit
        }

        # Exception Handling
        try:
            choice = int(input(">> "))
            if choice in input_choice:
                input_choice[choice]()
            else:
                print("ERROR | out_of_bounds_input")

        except ValueError:
            print("ERROR | invalid_input")

default = Bank("", "")
#default.Menu() # [PROGRAM]
default.BankMenu() # [DEBUGGING]
