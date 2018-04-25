from account import Account


class CheckingAccount(Account):
    def __init__(self, holder, accnumber, sbal, overdraft_limit):
        Account.__init__(self, holder, accnumber, sbal)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def withdraw(self, amount):
        amount_allowed = self.get_balance() + self.get_overdraft_limit()
        if amount_allowed >= amount > 0:
            self.balance -= amount
            return True
        return False
