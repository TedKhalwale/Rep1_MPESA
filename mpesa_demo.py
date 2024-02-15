# This program is a basic replicated design of the M-pesa code.
#Create the M-PESA class
class MPESA:
    def __init__(self):
        self.accounts = {
            "10203040": 20500,
            "90807060": 26800,
            "31447249": 25890,
        }
        
# A way of registering someone's account into the system.
    def register(self, acc_number, acc_balance=0):
        if acc_number in self.accounts:
            print("Sorry. Account already exists!")
        else:
            self.accounts[acc_number] = acc_balance
            print("Account successfully registered.")
# A way of depositing money into the account.
    def deposit(self, acc_number, amount):
        if acc_number not in self.accounts:
            print("Sorry. Account does not exist!")
        else:
            acc_balance = acc_balance + amount     #self.accounts[acc_number]
            print("Deposit successful. Your new account balance is: ", acc_balance)
# A way of withdrawing money from the account
    def withdraw(self, acc_number, amount):
        if acc_number not in self.accounts:
            print("Sorry. Account doesn't exist!")
        elif amount > self.accounts[acc_number]: 
            print("Sorry, There are insufficient funds in the account.")
        else:
            acc_balance = acc_balance - amount
            print("Withdrawal successful. Your new account balance is:", acc_balance)
# A way to check the balance in one's account       
    def check_balance(self, acc_number):
        print("Your account balance is:", self.accounts[acc_number])
# A way to fululiza / take a loan    
    def fululiza(self, acc_number, amount):
        if acc_number not in self.accounts:
            print("Sorry. Account doesn't exist!")
        elif amount > 18000:
            print("Sorry. Request denied. Amount too large")
        else:
            acc_balance = self.accounts[acc_number] + amount
            print("Fululza request accepted. New MPESA balance: ", self.accounts[acc_number])

                                                                
# Instantiate the class
MPESA_accounts = MPESA()


# A loop to keep the program running
while True:
    print("\nWelcome.")
    print("1. Register an account ")
    print("2. Deposit money into an account")
    print("3. Withdraw money from an account")
    print("4. check balance in your account")
    print("5. Fululiza")
    print("6. Exit")

# Prompt the user to choose one
    pick = input("Choose your pick: ")

# Perform  an action corresponding to the user's choice

    if pick == '1':
        acc_number = input("Enter account number: ")
        MPESA_accounts.register(acc_number)
    elif pick in ['2', '3', '4', '5']:
        acc_number = input("Enter account number: ")
        if acc_number not in MPESA_accounts.accounts:
            print("Sorry. Account doesn't exist!")
          # continue
        if pick == '2':
            amount = float(input("Enter amount to deposit: "))
            MPESA_accounts.deposit(acc_number, amount)
        elif pick == '3':
            amount = float(input("Enter amount to withdraw: "))
            MPESA_accounts.withdraw(acc_number, amount)
        elif pick == '4':
            MPESA_accounts.check_balance(acc_number)
        elif pick == '5':
            fululiza_amount = float(input("Enter amount you want to fululiza: "))
            MPESA_accounts.fululiza(acc_number, fululiza_amount)
    elif pick == '6':
         print("Thank you for using MPESA. See you again")
         break

    else:
         print("Invalid pick. Try again!")
        
    







    
                