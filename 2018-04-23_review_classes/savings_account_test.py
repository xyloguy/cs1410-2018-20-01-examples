import unittest
from unittest import TestCase, main
from savings_account import SavingsAccount
import sys


class SavingsAccountTestCase(TestCase):
    def setUp(self):
        self.holder = 'John'
        self.account_number = 12345
        self.starting_balance = 1500
        self.interest_rate = 0.01
        self.account = SavingsAccount(self.holder, self.account_number, self.starting_balance, self.interest_rate)

    def test_create_account(self):
        self.assertEqual(self.holder, self.account.get_holder())
        self.assertEqual(self.account_number, self.account.get_account_number())
        self.assertEqual(self.starting_balance, self.account.get_balance())
        self.assertEqual(self.interest_rate, self.account.get_interest_rate())

    @unittest.skipIf(not sys.platform.startswith('darwin'), 'Only run on mac')
    def test_001_mac(self):
        self.fail('You are on a mac')
        pass

    @unittest.skipIf(not sys.platform.startswith('linux'), 'Only run on linux')
    def test_001_linux(self):
        pass

    def test_interest_rate_works(self):
        a = self.account
        m_rate = self.interest_rate / 12
        added = self.starting_balance * m_rate

        self.assertEqual(self.starting_balance, a.get_balance())
        self.assertEqual(added, a.add_monthly_interest())
        self.assertEqual(self.starting_balance + added, a.get_balance())


if __name__ == '__main__':
    main()
