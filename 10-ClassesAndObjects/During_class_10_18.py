class acc():
    def __init__(self, account):
        self.account = account
        self.balance = 0
        
    def deposit(self, deposit):
        self.balance+=deposit
        
    def withdraw(self, withdraw):
        if self.balance>=withdraw:
            self.balance-=withdraw
        
    def show(self):
        print(f"Account balance: {self.balance} PLN")
        
acc1=acc("12 3456 5555 9090 1111 0000 7722")
acc1.show()
acc1.deposit(25.3)
acc1.show()
acc1.withdraw(31.7)
acc1.show()
acc1.withdraw(14)
acc1.show()

        