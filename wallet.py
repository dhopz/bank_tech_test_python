import datetime

class InsufficientAmount(Exception):
    pass

class Wallet():

    def __init__(self,initial_amount=0,transactions=[]):
        self.balance = initial_amount
        self.transactions = transactions

    def deposit(self,funds):
        self.balance += funds
        self.transactions.append({'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':funds, 'balance': self.balance})

    def withdraw(self,funds):
        if self.balance < funds:
            raise InsufficientAmount("Withdrawal for {} exceeds Wallet Balance".format(funds))
        self.balance -= funds
        self.transactions.append({'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':funds, 'balance': self.balance})