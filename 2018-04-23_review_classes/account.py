class Account:
    def __init__(self, holder, account_number, starting_balance):
        self.holder = holder
        self.number = int(account_number)
        self.balance = float(starting_balance)

    def get_holder(self):
        return self.holder

    def get_account_number(self):
        return self.number

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.get_balance() >= amount > 0:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def __add__(self, other):
        balance = self.get_balance() + other.get_balance()
        account_number = (self.get_account_number() + other.get_account_number()) // 2
        holder = self.get_holder() + ' and ' + other.get_holder()
        return Account(holder, account_number, balance)

if __name__ == '__main__':
    a = Account('John', 123, 1500.05)
    print(a.get_holder())
    print(a.get_account_number())
    print(a.get_balance())
    print(a.withdraw(500))  # True
    print(a.withdraw(-10))  # False
    print(a.withdraw(0))  # False
    print(a.withdraw(1000.05))  # True
    print(a.get_balance())
    print(a.deposit(-10))  # False
    print(a.deposit(0))  # False
    print(a.deposit(252))  # True
    print(a.get_balance())
