from banking import Account, Person

def test_account():
    test = Account(60, "tester")

    print("Try to add to much interest")
    test.interest(70)
    print("Attempt to over withdrawl account")
    test.withdrawl(70)
    test.withdrawl(60)
    print("Withdrawl almosteverything.", test.pretty_balance())
    test.deposit(60)
    print("New Balanmce should be 63:")
    print(test.pretty_balance())

def test_person():
    test = Person("max", "resnick", "max@max.com")
    print(test.open_account(500, "the test"))
    for account in test.accounts:
        print(account)
    print(test.close_account("the test"))
    print(test.close_account("the waka"))


from banking import Bank

test = Bank()

test.new_customer("max", "resnick", "test@test.com")

test.make_customer_account("test@test.com","test", 50)
Your new account has been succesfully created.
