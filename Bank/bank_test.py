from unittest import TestCase

import pytest

from Bank import bank
from Bank.exceptions.InsufficientBalance import InsufficientBalance
from Bank.exceptions.InvalidAccount import InvalidAccount
from Bank.exceptions.WrongPinException import WrongPinException


class TestSomething(TestCase):
    def test_for_the_creation_of_an_account_from_the_bank(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        self.assertEqual(1, gtBank.total_account())
        self.assertEqual('1', account1.get_account_number())

    def test_that_bank_create_two_account_and_account_number_is_1_and_2(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        account2 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        self.assertEqual(2, gtBank.total_account())
        self.assertEqual('1', account1.get_account_number())
        self.assertEqual('2', account2.get_account_number())

    def test_that_bank_creates_two_account_and_find_those_account_by_their_account_number(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        account2 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        self.assertEqual(2, gtBank.total_account())
        self.assertEqual(account1, gtBank.find_account('1'))
        self.assertEqual(account2, gtBank.find_account('2'))

    def test_that_bank_create_two_accounts_and_find_an_account_with_non_existing_account_number_throws_exception(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        account2 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        self.assertEqual(2, gtBank.total_account())
        with pytest.raises(InvalidAccount) as bank_info:
            gtBank.find_account("3")
        assert str(bank_info.value) == 'Invalid Account'

    def test_that_bank_can_find_an_account_and_deposit_1k_into_the_customer_account_balance_is_1k(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'pin')
        gtBank.deposit('1', 1000)
        self.assertEqual(1, gtBank.total_account())
        self.assertEqual(1000, account1.check_balance("pin"))

    def test_that_bank_can_create_account_and_deposit_2k_into_the_account_with_wrong_account_number(self):
        gtBank = bank.Bank()
        account = gtBank.creatAccount('first_name', 'last_name', 'pin')
        with pytest.raises(InvalidAccount) as bankInfo:
            gtBank.deposit('2', 2000)
        assert str(bankInfo.value) == 'Invalid Account'
        self.assertEqual(0, account.check_balance('pin'))

    def test_that_bank_can_create_account_deposit_2k_into_account_withdraw_800_balance_is_12k(self):
        gtBank = bank.Bank()
        account = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        gtBank.deposit('1', 2000)
        gtBank.withdraw('1', 'correct_pin', 800)
        self.assertEqual(1200, account.check_balance('correct_pin'))

    def test_that_we_create_an_account_deposit_1k_and_withdraw_5h_with_wrong_pin_throw_exception(self):
        gtBank = bank.Bank()
        account = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        gtBank.deposit('1', 1000)
        with pytest.raises(WrongPinException) as bankInfo:
            gtBank.withdraw('1', 'wrong_pin', 500)
        assert str(bankInfo.value) == 'Wrong pin'
        self.assertEqual(1000, account.check_balance('correct_pin'))

    def test_that_bank_can_create_two_account_and_deposit_2k_to_account1_and_transfer_1k_from_account1_to_account2(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        account2 = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        gtBank.deposit('1', 2000)
        gtBank.transfer('1', '2', 'correct_pin', 1000)
        self.assertEqual(1000, account1.check_balance('correct_pin'))
        self.assertEqual(1000, account2.check_balance('correct_pin'))

    def test_that_bank_can_create_two_account_and_deposit_2k_to_account1_and_transfer_3k_throws_exceptions(self):
        gtBank = bank.Bank()
        account1 = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        account2 = gtBank.creatAccount('first_name', 'last_name', 'correct_pin')
        gtBank.deposit('1', 2000)
        with pytest.raises(InsufficientBalance) as bankInfo:
            gtBank.transfer('1', '2', 'correct_pin', 3000)
        assert str(bankInfo.value) == 'Insufficient balance'
        self.assertEqual(2000, account1.check_balance('correct_pin'))
