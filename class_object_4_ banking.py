#4. Banking account
class Account:
    def __init__(self, title,balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

acc = SavingsAccount("Ashish", 5000,5)
print(acc.title)   #output- Ashish
print(acc.balance) #output - 5000
print(acc.interest_rate)  #output- 5