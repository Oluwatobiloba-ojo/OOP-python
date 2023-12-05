from unittest import TestCase
import pytest
from src.Bank import account
from src.Bank.exceptions.InsufficientBalance import InsufficientBalance
from src.Bank.exceptions.InvalidAmountException import InvalidAmountException
from src.Bank.exceptions.WrongPinException import WrongPinException


class TestSomething(TestCase):
    def test_that_account_can_deposit_1k_and_balance_is_1k(self):
        user_account = account.Account('first_name', "account_number", "correct_pin")
        user_account.deposit(1000)
        self.assertEqual(1000, user_account.check_balance('correct_pin'))

    def test_that_account_can_deposit_1k_and_2k_and_balance_is_3k(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        user_account.deposit(1000)
        user_account.deposit(2000)
        self.assertEqual(3000, user_account.check_balance('correct_pin'))

    def test_that_when_i_depositMinus1k_throws_invalid_amount_exception(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        with pytest.raises(InvalidAmountException) as accountInfo:
            user_account.deposit(-1000)
        assert str(accountInfo.value) == 'Invalid Amount'

    def test_that_when_i_deposit_1k_and_check_balance_with_a_wrong_pin_throw_exception(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        user_account.deposit(1000)
        with pytest.raises(WrongPinException) as accountInfo:
            user_account.check_balance("wrong_pin")
        assert str(accountInfo.value) == 'Wrong pin'

    def test_for_when_i_deposit_1k_and_withdraw_5h_balance_is_5h(self):
        user_account = account.Account("first_name", 'account_number', 'correct_pin')
        user_account.deposit(1000)
        user_account.withdraw('correct_pin', 500)
        self.assertEqual(user_account.check_balance('correct_pin'), 500)

    def test_that_when_i_deposit_1k_and_withdraw_5h_with_a_wrong_pin_throws_exception(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        user_account.deposit(1000)
        with pytest.raises(WrongPinException) as accountInfo:
            user_account.withdraw('wrong_pin', 500)
        assert str(accountInfo.value) == 'Wrong pin'
        self.assertEqual(1000, user_account.check_balance('correct_pin'))

    def test_that_when_i_deposit_1k_and_withdraw_minus_5h_throws_an_exception(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        user_account.deposit(1000)
        with pytest.raises(InvalidAmountException) as accountInfo:
            user_account.withdraw('correct_pin', -500)
        assert str(accountInfo.value) == 'Invalid Amount'
        self.assertEqual(1000, user_account.check_balance('correct_pin'))

    def test_when_i_deposit_2k_and_want_to_withdraw_3k_throws_exceptions(self):
        user_account = account.Account('first_name', 'account_number', 'correct_pin')
        user_account.deposit(2000)
        with pytest.raises(InsufficientBalance) as accountInfo:
            user_account.withdraw('correct_pin', 3000)
        assert str(accountInfo.value) == 'Insufficient balance'
        self.assertEqual(2000, user_account.check_balance('correct_pin'))
