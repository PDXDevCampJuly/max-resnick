""" A simplified banking module. """


class Account:
    """
    An account class.
    """
    def __init__(self, balance, account_type="checking"):
        self.balance = balance
        self.account_type = account_type

    def deposit(self, money):
        self.balance += money
        return self.check_balance()

    def withdrawl(self, money):
        if money <= self.balance:
            self.balance -= money
            return self.check_balance()
        else:
            print("You may not withdrawl more than\
                  your current balance of:", self.pretty_balance())

    def check_balance(self):
        return self.balance

    def pretty_balance(self):
        """
        Returns a string representation of the balance for pretty print.
        """
        return ("${:,.2f}".format(self.balance))

    def interest(self, percentage):
        if percentage > 1 and self.account_type == 'checking':
            return "The percentage should be set a fraction and\
            is available only for savings type accounts."
        else:
            self.balance += self.balance * percentage
            return self.check_balance()


class Person:
    """
    A person class.
    """
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}

    def open_account(self, initial_balance, account_name,
                     account_type="checking"):
        name_length = len(account_name)
        if initial_balance > 0 and name_length > 0:
            new_account = Account(initial_balance,  account_type)
            self.accounts[account_name] = new_account
            return self.accounts
        if initial_balance <= 0:
            error = "A min. deposit of $.01 is required. \n"
        if name_length <= 0:
            error += "A name is required for the account"
        return {"error": error}

    def close_account(self, name):

        if name in self.accounts:
            del self.accounts[name]
            return "Account Deleted."
        else:
            return "Account doesn't exist."

    def full_name(self):
        """
        Nicety, returns the full_name of the person.
        """
        return self.first_name + self.last_name

    def get_accounts(self):
        return self.accounts

class Bank:
    """
    The instituion class.
    """
    def __init__(self, savings_interest=.03):
        self.savings_interest = savings_interest
        self.customers = {}

    def _is_valid_account(self, email):
        if email in self.customers:
            return True
        else:
            return False

    def monthly_interest(self):
        pass

    def new_customer(self, first_name, last_name, email):
        new_customer = Person(first_name, last_name, email)
        self.customers[email] = new_customer

    def remove_customer(self, email, secure_remove=False):
        if self._is_valid_account(email) and secure_remove:
            # TODO this isn't entirely correct,
            for account in enumerateself.customers[email].get_acounts():
                del account
        elif email in self.customers:
            del self.customers[email]

    def show_customer_info(self, email):
        if self._is_valid_account(email):
            customer_accounts = self.customers[email].get_accounts()
            for account in customer_accounts:
                balance = customer_accounts[account].pretty_balance
                message = "\t - {1} has a balance of {2}\n"
                print(message.format(message.format(account, balance)))
        else:
            print("Invalid account.")

    def customer_worth(self):
        pass

    def customer_deposit(self):
        pass

    def customer_withdrawl(self):
        pass

    def make_customer_account(self, email, nickname, initial_deposit,
                              account_type="checking"):
        """
        Create new account, check for error, print error.
        """
        if self._is_valid_account(email):
            new_account = self.customers[email].open_account(initial_deposit,
                                                             nickname,
                                                             account_type)
        else:
            new_account = {"error": "No customer {} found.".format(email)}

        # TODO this doesn't print mulitple error messages well.
        # it doesn't but it will be ugly.
        if "error" in new_account:
            print("The following errors have occured:")
            print("\t - {}".format(new_account["error"]))
        else:
            print("Your new account has been succesfully created.")

    def remove_customer_acount(self):
        """
        use the account class method to remove, check for valid email in customers.dict.

        """
        pass
