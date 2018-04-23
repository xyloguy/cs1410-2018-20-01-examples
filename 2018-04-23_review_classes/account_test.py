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





if __name__ == '__main__':
    main()
