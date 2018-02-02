class BankAccount:
    def __init__(self, person, balance):
        self.owner = person
        self.balance = float(balance)

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        if 0 < amount:
            self.balance += amount

    def __str__(self):
        return str(self.owner) + ', Balance: $' + str(round(self.get_balance(), 3))