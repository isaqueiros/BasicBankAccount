class Account:
    def __init__(self, owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f'Name: {self.owner}; \nBalance: £{self.balance}.'
    def __owner__(self):
        return self.owner
    def __balance__(self):
        return self.balance

    def Deposit(self,value):
        self.balance=self.balance + value
        print("Deposit Accepted")
        print(f'Your current balance is £{self.balance}')

    def Withdraw(self,amount):
        if self.balance < amount:
            print('Funds Unavailable!')
            print(f'You only have £{self.balance} available.')
        else:
            print("Withdraw Accepted")
            print(f'Your current balance is £{self.balance}')