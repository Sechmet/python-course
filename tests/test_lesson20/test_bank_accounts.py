import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson20'))
from bank_accounts import BankAccount, InterestRewardsAcct, SavingsAcct, BalanceException
import io
from contextlib import redirect_stdout


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account = BankAccount(1000, 'Dave')

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_account_name(self):
        self.assertEqual(self.account.name, 'Dave')

    def test_deposit(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw_insufficient_funds(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.withdraw(2000)
        self.assertEqual(self.account.balance, 1000)

    def test_viable_transaction_raises(self):
        with self.assertRaises(BalanceException):
            self.account.viable_transaction(2000)

    def test_transfer(self):
        f = io.StringIO()
        with redirect_stdout(f):
            other = BankAccount(500, 'Sara')
            self.account.transfer(200, other)
        self.assertEqual(self.account.balance, 800)
        self.assertEqual(other.balance, 700)


class TestInterestRewardsAcct(unittest.TestCase):

    def setUp(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account = InterestRewardsAcct(1000, 'Dave')

    def test_deposit_with_interest(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.deposit(100)
        self.assertEqual(self.account.balance, 1105)


class TestSavingsAcct(unittest.TestCase):

    def setUp(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account = SavingsAcct(1000, 'Dave')

    def test_withdraw_with_fee(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.withdraw(100)
        self.assertEqual(self.account.balance, 895)

    def test_withdraw_insufficient_with_fee(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.account.withdraw(1000)
        self.assertEqual(self.account.balance, 1000)


if __name__ == "__main__":
    unittest.main()