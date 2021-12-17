class Wallet():

    def __init__(self,initial_amount=0,transactions=[]):
        self.balance = initial_amount
        self.transactions = transactions