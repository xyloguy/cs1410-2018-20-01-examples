# from account import Account
# from checking_account import CheckingAccount
# from savings_account import SavingsAccount


def account_type():
    while True:
        print('What type of account would you like to track?')
        account_types = {
            'a': 'Generic Account',
            'c': 'Checking Account',
            's': 'Savings Account',
        }
        for key, value in account_types.items():
            print('[{}] {}'.format(key, value))

        ask = input('Enter an option: ')

        if ask.lower() in account_types:
            return ask.lower()

        else:
            print('Invalid Option')
            print('')


def main():
    account_choices = ['a', 's', 'c']
    ask = account_type()
    print(ask)


if __name__ == '__main__':
    main()