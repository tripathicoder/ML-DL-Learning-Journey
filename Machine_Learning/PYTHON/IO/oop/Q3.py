class Account:
    def __init__(self,  balance,account_number):
        self.balance=balance
        self.account_number=account_number
    def deposit(self, amount):
        self.balance+=amount
        def credit(self,account_number,amount):
            if self.account_number == account_number:
                self.balance-=amount

        