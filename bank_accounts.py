class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount: int, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount: '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount: int):
        self.balance += amount
        print("Deposit complete")
        self.getBalance()

    def viableTransaction(self, amount: int):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of $'{self.balance:.2f}'")

    def withdraw(self, amount: int):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount:int, account):
        try:
            print("\n************\n\nBeginning "
                  "Transfer.. 🧨")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! 🎗🎗\n\n"
                  "**************")
        except BalanceException as error:
            print(f"\nTransfer interrupted. 🎇 {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount: int):
        self.balance += amount*1.05
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount: int):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")