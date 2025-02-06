class bak():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(amount > self.balance):
            print(f"You have only: {self.balance}tg. Try again!")
        else:
            self.balance -= amount
    def __str__(self):
        return f"name: {self.owner} \n balance: {self.balance}"
a = bak("Kirill", 100000)
print(a)

a.deposit(25000)
print(a)

a.withdraw(250000)
print(a)

a.withdraw(75000)
print(a)

