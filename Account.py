class Account():
    def __init__(self, id, accountno, accounttype, balance):
        
        self.id = id
        self.accountno = accountno
        self.accounttype = accounttype
        self.balance = balance
    
    def __str__(self):
        return str(self.id) + " " + str(self.accountno) + " " + str(self.accounttype) + " " + str(self.balance)

    def __repr__(self):
        return "{}:{}:{}".format(self.accountno, self.accounttype, self.balance)