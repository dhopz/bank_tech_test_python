import datetime
import transaction

class InsufficientAmount(Exception):
    pass

class Wallet():

    def __init__(self,initial_amount=0,transactions=[]):
        self.balance = initial_amount
        self.transactions = transactions

    def transaction(self,transaction_type,funds):
        if transaction_type == "Deposit":
            self.balance += funds
        else:               
            if self.balance < funds:
                raise InsufficientAmount("Withdrawal for {} exceeds Wallet Balance".format(funds))
            else:
                self.balance -= funds
        self.transactions.append({'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':funds, 'balance': self.balance, 'type':transaction_type})



        


    def deposit(self,funds):
        self.balance += funds
        self.transactions.append({'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':funds, 'balance': self.balance})

    def withdraw(self,funds):
        if self.balance < funds:
            raise InsufficientAmount("Withdrawal for {} exceeds Wallet Balance".format(funds))
        self.balance -= funds
        self.transactions.append({'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':funds, 'balance': self.balance})