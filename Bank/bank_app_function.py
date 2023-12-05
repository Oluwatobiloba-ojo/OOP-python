from Bank.bank import Bank

union_bank = Bank()


def bank_main():
    main = """
             ==================================
             1 -> Create Account
             2 -> Deposit Account
             3 -> Transfer Account
             4 -> Check Balance
             5 -> Withdraw
             ===================================
             """
    response = int(input(main))
    bank_operation(response)


def bank_operation(inputs):
    if inputs == 1:
        create_account()
    elif inputs == 2:
        deposit_into_account()
    elif inputs == 3:
        transfer_to_account()
    elif inputs == 4:
        check_balances()
    elif inputs == 5:
        withdraw_from_account()


def create_account():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    pin = input("Enter the pin you desired: ")
    account = union_bank.creatAccount(first_name, last_name, pin)
    print(account.toString())
    bank_main()


def deposit_into_account():
    account_number = input("Enter your account number: ")
    amount = int(input("Enter the amount you want to deposit into: "))
    try:
        union_bank.deposit(account_number, amount)
        print(union_bank.find_account(account_number).toString())
        print("Deposit Successfully done")
        bank_main()
    except Exception:
        print('Invalid deposit')
        bank_main()


def transfer_to_account():
    sender_account = input("Enter your account number: ")
    receiver_account = input("Enter the receiver account: ")
    pin = input("Enter your pin: ")
    amount = int(input("Enter the amount you want to transfer in to "))
    try:
        union_bank.transfer(sender_account, receiver_account, pin, amount)
        print(union_bank.find_account(sender_account).toString())
        print("Transaction Successfully ")
        bank_main()
    except Exception:
        print("Invalid transaction: ")
        bank_main()


def check_balances():
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")
    try:
        account = union_bank.find_account(account_number)
        print("Your balance is ", account.check_balance(pin))
        bank_main()
    except Exception:
        print("Wrong pin")
        bank_main()


def withdraw_from_account():
    account_number = input("Enter your account number: ")
    account_pin = input("Enter your pin: ")
    amount = int(input("Enter the amount you want to withdraw: "))
    try:
        union_bank.withdraw(account_number, account_pin, amount)
        print(union_bank.find_account(account_number).toString())
        bank_main()
    except Exception:
        print("Invalid withdrawal transaction")
        bank_main()
