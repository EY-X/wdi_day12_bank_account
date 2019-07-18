class BankAccount:
    interest_rate = float(.5)
    accounts = []

    def __init__(self):
        self.balance = 0

    def deposit(self, number):
        self.balance += number

    def withdraw(self, number):
        self.balance -= number


    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
          total += account.balance
        return total

    @classmethod
    def interest_time(cls):
        total = 0
        for account in cls.accounts:
            total += (cls.interest_rate * account.balance)
        return total


my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0



# eden = BankAccount.create()

# eden.deposit(100)
# print(eden.balance)

# john = BankAccount.create()
# john.withdraw(50)
# print(john.balance)

# print(BankAccount.total_funds())


