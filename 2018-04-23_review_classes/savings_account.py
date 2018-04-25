from account import Account


class SavingsAccount(Account):
    def __init__(self, holder, accnumber, sbal, interest_rate):
        Account.__init__(self, holder, accnumber, sbal)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def add_monthly_interest(self):
        m = self.get_interest_rate() / 12
        added = self.balance * m
        self.balance += added
        return added
