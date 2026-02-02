# Bank Account Class
class BankAccount:
    def __init__(self,account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    def validate_pin(self,entered_pin):
        return entered_pin == self.__pin
    
    def check_balance(self):
        print(f'you account current balance {self.__balance}')

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            print(f'the amount {amount} deposied sucessfully')
        else:
            print('Invalid account number')
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'the amount {amount} withdrawed sucessfully')
        else:
            print('Insuffcient balance')
    
    def change_pin(self,old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) ==4 and new_pin.isdigit():
            self.__pin = new_pin
            print('Pin changed sucessfully')
        else:
            print('Failed to change the pin')
        

class Atm:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input('enter your account number : ')
        pin = input('enter your pin : ')
        if len(pin) == 4 and pin.isdigit():
            # Store a new BankAccount object in the accounts dictionary
            self.accounts[account_number] = BankAccount(account_number, pin)
            print('Account created sucessfully')
        else:
            print('Invalid pin. Pin must be 4 digits')
    
    def authenticate_account(self):
        account_number = input('Enter your account number: ')
        pin_input = input('Enter your pin: ')

        # check if amount exists in dictionary
        if account_number in self.accounts:
            account = self.accounts[account_number]
            # check if the pin is correct for that specific account
            if account.validate_pin(pin_input):
                print('Authentication successful')
                self.account_menu(account)
            else:
                print('Invalid pin')
        else:
            print('Account not found')

    def account_menu(self, account):
        while True:
            print('\n---- ACCOUNT MENU ---')
            print('1. Check Balance')   
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Change Pin')
            print('5. Logout')

            choice = input('Enter your choice(1-5): ')

            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input('Enter the amount to deposit: '))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input('Enter the amount to withdraw: '))
                account.withdraw(amount)
            elif choice == '4':
                old_pin = input('Enter your old pin: ')
                new_pin = input('Enter your new pin: ')
                account.change_pin(old_pin, new_pin)
            elif choice == '5':
                print('Exiting the program')
                break
            else:
                print('Invalid choice. Please try again')
    
    def main_menu(self):
        while True:
            print('\n---- ATM MAIN SYSTEM ---')
            print('1. Create Account')
            print('2. Acess Account')
            print('3. Exit')

            choice = input('Enter your choice(1-3): ')

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.authenticate_account()
            elif choice == '3':
                print('Exiting the program')
                break
            else:
                print('Invalid choice. Please try again')

if __name__ == '__main__':
    atm = Atm()
    atm.main_menu()