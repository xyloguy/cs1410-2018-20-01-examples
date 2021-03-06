from unittest import TestCase, main
from account import Account


class AccountTestCase(TestCase):
    def create_account(self):
        self.holder = 'John'
        self.account_number = 12345
        self.balance = 1500
        return Account(self.holder, self.account_number, self.balance)

    def test_create_account(self):
        a = self.create_account()
        self.assertEqual(self.holder, a.get_holder())
        self.assertEqual(self.account_number, a.get_account_number())
        self.assertEqual(self.balance, a.get_balance())

    def test_withdraw_works(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertTrue(a.withdraw(500))
        self.assertEqual(self.balance - 500, a.get_balance())

    def test_withdraw_fails_negative(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.withdraw(-500))
        self.assertEqual(self.balance, a.get_balance())

    def test_withdraw_fails_zero(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.withdraw(0))
        self.assertEqual(self.balance, a.get_balance())

    def test_withdraw_fails_too_much(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.withdraw(self.balance + .000000001))
        self.assertEqual(self.balance, a.get_balance())

    def test_deposit_fail_negative(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.deposit(-1))
        self.assertEqual(self.balance, a.get_balance())

    def test_deposit_fail_zero(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.deposit(0))
        self.assertEqual(self.balance, a.get_balance())

    def test_deposit_good(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertTrue(a.deposit(10000000))
        self.assertEqual(self.balance + 10000000, a.get_balance())

    def test_join_accounts(self):
        a = self.create_account()
        holder = 'Jaime'
        account_number = 5
        balance = 10000
        b = Account(holder, account_number, balance)
        c = a + b
        self.assertEqual('John and Jaime', c.get_holder())
        self.assertEqual((a.get_account_number() + b.get_account_number()) // 2, c.get_account_number())
        self.assertEqual(a.get_balance() + b.get_balance(), c.get_balance())


if __name__ == '__main__':
    main()
