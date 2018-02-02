import person
from bank_account import BankAccount

joe = person.Person('Joe', '123-45-6789')
print(joe)
account = BankAccount(joe, 1200.49)
print(account.get_balance())
print(account.owner.get_ssn())
