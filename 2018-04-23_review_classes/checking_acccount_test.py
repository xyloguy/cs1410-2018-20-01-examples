from unittest import TestCase, main
from checking_account import CheckingAccount


class CheckingAccountTestCase(TestCase):
    def create_account(self):
        self.holder = 'John'
        self.account_number = 12345
        self.balance = 1500
        self.overdraft_limit = 100
        return CheckingAccount(self.holder, self.account_number, self.balance, self.overdraft_limit)

    def test_create_account(self):
        a = self.create_account()
        self.assertEqual(self.holder, a.get_holder())
        self.assertEqual(self.account_number, a.get_account_number())
        self.assertEqual(self.balance, a.get_balance())
        self.assertEqual(self.overdraft_limit, a.get_overdraft_limit())

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

    def test_withdraw_overdraft(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertTrue(a.withdraw(self.balance + self.overdraft_limit))
        self.assertEqual(-1 * self.overdraft_limit, a.get_balance())

    def test_withdraw_overdraft_fails(self):
        a = self.create_account()
        self.assertEqual(self.balance, a.get_balance())
        self.assertFalse(a.withdraw(self.balance + self.overdraft_limit + 1))
        self.assertEqual(self.balance, a.get_balance())


if __name__ == '__main__':
    main()
