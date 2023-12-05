from src.Bank import account
from src.Bank.exceptions.InvalidAccount import InvalidAccount


def concatenate(first_name, last_name):
    return first_name + " " + last_name


class Bank:

    def __init__(self):
        self._total_accounts = 0
        self._lists_of_account = []

    def creatAccount(self, first_name, last_name, pin):
        self._total_accounts += 1
        full_name = concatenate(first_name, last_name)
        number = self.generate_account_number()
        accounts = account.Account(full_name, number, pin)
        self._lists_of_account.append(accounts)
        return accounts

    def total_account(self):
        return self._total_accounts

    def generate_account_number(self):
        return str(self._total_accounts)

    def find_account(self, account_number):
        for accounts in self._lists_of_account:
            if accounts.get_account_number() == account_number:
                return accounts
        raise InvalidAccount("Invalid Account")

    def deposit(self, account_number, amount):
        user_account = self.find_account(account_number)
        user_account.deposit(amount)

    def withdraw(self, account_number, pin, amount):
        user_account = self.find_account(account_number)
        user_account.withdraw(pin, amount)

    def transfer(self, sender_account_number, receiver_account_number, pin, amount):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)
        sender_account.withdraw(pin, amount)
        receiver_account.deposit(amount)
