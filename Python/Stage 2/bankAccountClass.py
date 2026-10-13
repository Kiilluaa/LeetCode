class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(self.name, "has", self.balance, "in their account.")

account1 = BankAccount("Alex")
account2 = BankAccount("Sam")

account1.deposit(100)
account1.withdraw(30)
account2.deposit(200)

account1.show_balance()
account2.show_balance()