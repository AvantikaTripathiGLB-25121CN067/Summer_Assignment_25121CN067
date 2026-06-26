class ATM:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Deposited:${amount}. Current balance:${self.balance}"
        else:
            return f"Invalid"
        
    def withdraw(self,amount):
        if 0 < amount <=self.balance:
            self.balance -= amount
            return f" Withdrawn:${amount}. Current balance:${self.balance}"
        else:
            return f"Invalid"
        
    def check_balance(self):
        return f"Your current balance is:${self.balance}"
    
my_atm=ATM(20000)
print(my_atm.deposit(5000))
print(my_atm.check_balance())
print(my_atm.withdraw(1000))
