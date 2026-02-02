# attributes - are the values that belongs to class or object 
# methods - are the functions that belongs to class or object


# create an account with name with inital deposit
# deposit & withdraw fucntions

class Bank:
    _next_account_number = 100
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = self._validate_amount(balance)
        self.account_number = Bank._next_account_number
        Bank._next_account_number += 1
    

    # -------------- Validation Helpers ----------------------

    def _validate_amount(self,amount):
        if not isinstance(amount, (int,float)):
            raise ValueError('Amount must be a number')
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        return amount
    
    def _validate_account(self,account_number):
        if account_number != self.account_number:
            raise ValueError('Invalid account number')

    def deposit(self,account_number,deposit_amount):
        self._validate_account(account_number)
        amount = self._validate_amount(deposit_amount)
        
        self.balance += amount
        return {
            "message": f"{amount} has been deposited successful",
            "new_balance": self.balance
        }
    def withdraw(self,account_number,withdraw_amount):
        self._validate_account(account_number)
        amount = self._validate_amount(withdraw_amount)

        if amount > self.balance:
            raise ValueError('Insufficient balance')

        self.balance -= amount
        return{
            "message": f"{amount} has been withdrawn successful",
            "new_balance": self.balance
        }

    def show_account(self):
        return {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "balance": self.balance
        }
    

def display():
    print("\n---- Welcome to Our Bank ----")
    print("1. Create an Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account Details")
    print("5. Exit")
    print("------------------------------")


def main():
    accounts = {}   # Dictionary to store multiple accounts

    while True:
        display()
        choice = input("Enter your choice: ")

        # ---------------------------------------------------------------------
        # 1. CREATE ACCOUNT
        # ---------------------------------------------------------------------
        if choice == "1":
            name = input("Enter account holder name: ")

            try:
                initial_balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid amount! Must be a number.")
                continue

            # Create account and save to dictionary
            acc = Bank(name, initial_balance)
            accounts[acc.account_number] = acc

            print("\nAccount created successfully!")
            print(f"Your account number is: {acc.account_number}")

        # ---------------------------------------------------------------------
        # 2. DEPOSIT
        # ---------------------------------------------------------------------
        elif choice == "2":
            if not accounts:
                print("No accounts exist! Create one first.")
                continue

            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))

                if account_number not in accounts:
                    print("Account not found!")
                    continue

                result = accounts[account_number].deposit(account_number, amount)
                print(result["message"])
                print("New Balance:", result["new_balance"])

            except Exception as e:
                print("Error:", e)

        # ---------------------------------------------------------------------
        # 3. WITHDRAW
        # ---------------------------------------------------------------------
        elif choice == "3":
            if not accounts:
                print("No accounts exist! Create one first.")
                continue

            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))

                if account_number not in accounts:
                    print("Account not found!")
                    continue

                result = accounts[account_number].withdraw(account_number, amount)
                print(result["message"])
                print("New Balance:", result["new_balance"])

            except Exception as e:
                print("Error:", e)

        # ---------------------------------------------------------------------
        # 4. SHOW ACCOUNT DETAILS
        # ---------------------------------------------------------------------
        elif choice == "4":
            if not accounts:
                print("No accounts exist!")
                continue

            try:
                account_number = int(input("Enter your account number: "))

                if account_number not in accounts:
                    print("Account not found!")
                    continue

                details = accounts[account_number].show_account()
                print("\n--- Account Details ---")
                print("Holder Name:", details["account_holder"])
                print("Account Number:", details["account_number"])
                print("Balance:", details["balance"])

            except Exception as e:
                print("Error:", e)

        # ---------------------------------------------------------------------
        # 5. EXIT
        # ---------------------------------------------------------------------
        elif choice == "5":
            print("Thank you for using our Banking System! Goodbye.")
            break

        else:
            print("Invalid choice! Enter a number between 1–5.")


# Run the program
if __name__ == "__main__":
    main()
