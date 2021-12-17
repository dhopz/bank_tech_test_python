import datetime
import wallet

class Statement():

    def __init__(self):        
        self.header = 'date || credit || debit || balance\n'

    def create_statement(self,transactions):
        first_line = [self.header]
        for i in transactions:
            if i['type'] == "Deposit":
                first_line.append(f"{i['date']} || {i['amount']} || || {i['balance']}\n")
            else:
                first_line.append(f"{i['date']} || || {i['amount']} || {i['balance']}\n")
        return "".join(first_line)



