class Account:
    interest=0.02
    def __init__(self,account_holder):
        self.balence=0
        self.holder=account_holder
    def deposit(self,amount):
        self.balence=self.balence+amount
        return self.balence
    def withdraw(self,amount):
        if amount > self.balence:
            return 'Insufficient funds'
        self.balence=self.balence-amount
        return self.balence

class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""
    withdraw_fee=1
    interest=0.01
    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_fee)
    
class Bank:
    """A bank *has* an account
    >>> bank=Bank()
    >>> john=bank.open_account('John',10)
    >>> jack=bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balence
    10.2"""
    def __init__(self):
        self.accounts=[]
    def open_account(self,holder,amount,kind=Account):
        account=kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balence*a.interest)
    def too_big_to_fail(self):
        return len(self.accounts)>1
