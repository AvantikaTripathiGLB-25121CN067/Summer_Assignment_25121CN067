class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Money deposited in {self.owner} account:${amount}. New balance:${self.balance}")

    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance-=amount
            print(f"Money withdrawn from {self.owner} account:${amount}. New balance:${self.balance}")

        else:
            print("Insufficient fund.")

acc=BankAccount("Amit",65000)
acc.deposit (2000)
acc.withdraw (1100)