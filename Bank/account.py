from Bank.exceptions.InsufficientBalance import InsufficientBalance
from Bank.exceptions.InvalidAmountException import InvalidAmountException
from Bank.exceptions.WrongPinException import WrongPinException


def validate(amount: int):
    if amount < 0:
        raise InvalidAmountException("Invalid Amount")


class Account:
    _balance = 0

    def __init__(self, first_name, account_number, pin):
        self._first_name = first_name
        self._number = account_number
        self._pin = pin

    def deposit(self, amount: int):
        validate(amount)
        self._balance += amount

    def check_balance(self, pin: str):
        self.validate_pin(pin)
        return self._balance

    def validate_pin(self, pin):
        if self._pin != pin:
            raise WrongPinException("Wrong pin")

    def withdraw(self, pin, amount):
        self.validate_pin(pin)
        validate(amount)
        self.validate_insufficient(amount)
        self._balance -= amount

    def validate_insufficient(self, amount):
        if amount > self._balance:
            raise InsufficientBalance("Insufficient balance")

    def get_account_number(self):
        return self._number

    def toString(self):
        return f'''
        ===================================
        Account name: {self._first_name}
        Account number: {self._number}
        Account Balance: {self._balance}
        Account pin: Unavailable
        ===================================
        '''
