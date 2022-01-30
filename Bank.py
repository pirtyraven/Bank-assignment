import re
from Customer import Customer
from Account import Account

class Bank():
    
    #customers = []
    id = []
    ctxt = "customers.txt"
    #customer_data = []
    #accounts = []
    accountNo = []
    #acc = []

    def __init__(self):
        self.name = "MyBank"
        self.customers = [] # listan kommer att fyllas på med Customer-objekt
        self.acc_list = [] # listan kommer att fyllas på med Account-objekt
        self._load() # laddar in själva textfilen eller "databasen"
        self.load_customers() # funktionen för att fylla customerslistan med Customer-objekt
        self.load_accounts() # funktionen för att fylla acc_list-listan med Account-objekt
           
    def _load(self):
        self.customer_data = []

        with open(self.ctxt) as txtFile:
            for x in txtFile:
                self.customer_data.append(x.strip())
        return self.customer_data

    def load_customers(self):
        for i in self.customer_data:
            y = i.replace("#", ":").split(":")
            cstmr = Customer(y[0], y[1], y[2])
            self.customers.append(cstmr)

        return self.customers

    def get_customers(self):

        for cstmr in self.customers:
            print(f"Name: {cstmr.name}, Social security number: {cstmr.pnr}")

    def get_customer(self, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False

        for i in self.customers:
            if pnr == i.pnr:
                the_customer = f"Customer id: {i.id}\nName: {i.name}\nSocial security number: {i.pnr}"
                the_accounts = ""

                for line in self.accounts:

                    if i.id in line.id:
                        the_accounts += f"Account number: {line.accountno}, Account type: {line.accounttype}, Balance: {line.balance}\n"

        print(f"{the_customer}\n\nAccounts: \n{the_accounts}")

    # def get_customer(self, pnr):
    #
    #     for i in self.customers:
    #         if pnr == i.pnr:
    #             x = str(i).split()
    #             y = x[0], x[1], x[2], x[3]
    #             id = y[0]
    #             for line in self.accounts:
    #                 if i.id in line.id:
    #                         self.acc.append(line)
    #                         z = re.sub(",", ":", str(self.acc))
    #                         t = str(z).strip().split(":")
    #                         if len(t) > 3:
    #                             firstacc = (f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
    #                             secondacc = (f"Second account: \n\tAccount no: {t[3]}\n\tAccount type: {t[4]}\n\tBalance: {t[5]}")
    #                         elif len(t) == 3:
    #                             firstacc = (f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
    #                             secondacc = (f"Second account: \n\tAccount no: {None}\n\tAccount type: {None}\n\tBalance: {None}")
    #
    #     print(f"Customer id: {y[0]}\nName: {y[1]} {y[2]}\nSocial security number: {y[3]}\n{firstacc}{secondacc}")
    def load_accounts(self):
        self.accounts = []
        account_data = {}

        for i in self.customer_data:
            x = i.replace("#",":").split(":")
            account_data[x[0]] = x[3:] # Skapar en dict med kund-id som key och kundens accounts som value
        for k, v in account_data.items():
            nr_acc = len(v)/3
            while nr_acc > 0:
                the_account = Account(str(k), v.pop(0), v.pop(0), v.pop(0))
                self.accounts.append(the_account)
                self.accountNo.append(the_account.accountno)
                nr_acc -= 1

        #print(self.accountNo)
        #print(self.accounts)


    def get_accounts(self):
        Bank.load_accounts(self)
        self.acc_list = []

        for i in self.accounts:
            account = f"{i.id} {i.accountno} {i.accounttype} {i.balance}"
            #account = str(i.id) + " " + str(i.accountno) + " " + i.accounttype + " " + str(i.balance)
            self.acc_list.append(account)
        print(self.acc_list)

    def get_account(self, pnr, acc_no):
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
        else:
            for x in self.customers:
                if pnr == x.pnr:
                    for y in self.accounts:
                        if acc_no == y.accountno and y.id == x.id:
                            return f'{y.accountno}, {y.accounttype}, {y.balance}'
                    return print(f"No account found with account number {acc_no}.")
            return print(f"No customer found with {pnr} in list")

    def add_account(self, pnr):
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            for i in self.customer_data:
                if pnr in repr(i):
                    index = self.customer_data.index(i)
                    line = f'{i}#{Bank.get_top_account(self)}:debit account:0.0'
                    new_line = i.replace(i, line)
                    self.customer_data[index] = new_line

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

        print("New account added!")

    def add_customer(self, name, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            print("Customer with same social security number already exists")
            return False
        else:
            textfile = open("customers.txt","a")
            textfile.write('\n' + Bank.get_new_id(self) + f':{name}:{pnr}:' + Bank.get_top_account(self) + f':debit account:0.0')
            textfile.close()
            return True

    def change_customer_name(self, newname, pnr):
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("\nSorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            for line in self.customer_data:
                if str(pnr) in line:
                    index = self.customer_data.index(line)
                    name = line.split(":")[1]
                    new_line = line.replace(name, newname)
                    self.customer_data[index] = new_line
                    print(f'Name changed from {name} to {newname}')

        else:
            print(f'\nNo customer with {pnr} exists')

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % l for l in self.customer_data)
    
    def remove_customer(self, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("\nSorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:   
            for line in self.customer_data:
                if pnr in line:
                    index = self.customer_data.index(line)
                    self.customer_data.pop(index)
                    for i in self.customers:
                        if pnr == i.pnr:
                            acc = ""
                            customer = f'Customer id: {i.id}\nName: {i.name}\nSocial security number: {i.pnr}\n'
                            for x in self.accounts:
                                if x.id == i.id:
                                    acc += f'\n\tAccount no: {x.accountno}\n\tAccount type: {x.accounttype}\n' \
                                           f'\tBalance returned: {x.balance}\n '

                            print(f'{customer}\nAccounts closed: {acc}')

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % l for l in self.customer_data)

    def deposit(self, pnr, id, amount):
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            Bank._load(self)
            for rad in self.customer_data:
                if pnr in repr(rad):
                    index = self.customer_data.index(rad)
                    r1 = rad.replace("#",":").split(":")
                    nyindex = r1.index(id)
                    old_bal = r1[nyindex+2]
                    #print(int(old_bal[:-2]))
                    new_bal = float(old_bal) + float(amount)
                    new_line = rad.replace(old_bal, str(new_bal))
                    self.customer_data[index] = new_line
                    print(f"Deposit successful! \nOld balance: {old_bal} \nNew balace: {new_bal}")
            with open(self.ctxt, "w") as f:
                f.writelines("%s\n" % l for l in self.customer_data)


    def withdrawal(self, pnr, id, amount):
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            Bank._load(self)
            for rad in self.customer_data:
                if pnr in repr(rad):
                    index = self.customer_data.index(rad)
                    r1 = rad.replace("#",":").split(":")
                    index2 = r1.index(id)
                    old_bal = r1[index2+2]
                    #print(int(old_bal[:-2]))
                    new_bal = float(old_bal) - float(amount)
                    if new_bal < 0:
                        print("Not enough money in account")
                        return False
                    new_line = rad.replace(old_bal, str(new_bal))
                    self.customer_data[index] = new_line
            print(f"Withdrawal successfull! \nOld balance: {old_bal} \nNew balace: {str(new_bal)}")
            with open(self.ctxt, "w") as f:
                f.writelines("%s\n" % l for l in self.customer_data)

    def close_account(self, pnr, acc_no):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            for line in self.customer_data:
                if pnr and acc_no in line:
                    index = self.customer_data.index(line)
                    if line.count("#") == 0:
                        print("Account removed. Customer has no more accounts and has therefor also been removed. Details below:\n")
                        Bank.remove_customer(self, pnr)
                        with open(self.ctxt, "w") as f:
                            f.writelines("%s\n" % l for l in self.customer_data)
                    elif line.count("#") > 0:
                        acc = Bank.get_account(self, pnr, acc_no).replace(", ", ":")
                        new_line = line.replace("#" + acc, "").replace(acc + "#", "")
                        self.customer_data[index] = new_line
                        print(f'Account with account number {acc.split(":")[0]} closed.\nType: {acc.split(":")[1]}\nBalance returned: {acc.split(":")[2]}')
                        with open(self.ctxt, "w") as f:
                            f.writelines("%s\n" % l for l in self.customer_data)

    def get_new_id(self):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            self.id.append(x[0])
        
        new_id = int(self.id[-1]) + 1
        
        return str(new_id)

    def get_top_account(self):

        Bank.get_accounts(self)    
        newAccount = int(max(self.accountNo)) + 1

        return str(newAccount)

m = Bank()
#m.load_accounts()
#m.close_account("139741-6173", "1002")