#from Account import Account
#from Customer import Customer
from Bank import Bank

mybank = Bank()


inp = True
while inp:
    print("\nPlease choose an action from the Menu:\n")
    print("1. Print list of customers, Name and pnr "
          "\n2. Add new customer "
          "\n3. Change customer name "
          "\n4. Delete customer "
          "\n5. Delete bank account "
          "\n6. See customer information (account numbers, balance, account types) "
          "\n7. Deposit money "
          "\n8. Withdraw money "
          "\n9. Add bank account "
          "\n10. Get account info "
          "\n11. Leave the bank\n")

    inp = input()

    if inp == "1":
        mybank.get_customers()
    elif inp == "2":
        name = input("Enter customers first and last name: ")
        pnr = input("Enter customers social security number: ")
        mybank.add_customer(name,pnr)
    elif inp == "3":
        newname = input("Enter new customer name, first and last name: ")
        pnr = input("Enter customers social security number: ")
        mybank.change_customer_name(newname,pnr)
    elif inp == "4":
        pnr = input("Enter customers social security number: ")
        mybank.remove_customer(pnr)
    elif inp == "5":
        pnr = input("Enter customers social security number: ")
        acc_no = input("Enter account number you wish to close: ")
        mybank.close_account(pnr, acc_no)
    elif inp == "6":
        pnr = input("Enter customers social security number: ")
        mybank.get_customer(pnr)
    elif inp == "7":
        pnr = input("Enter customers social security number: ")
        acc_no = input("Enter account number to which you would like to deposit: ")
        amount = input("Enter amount you would like to deposit: ")
        mybank.deposit(pnr, acc_no, amount)
    elif inp == "8":
        pnr = input("Enter customers social security number: ")
        acc_no = input("Enter account number from which you would like to withdraw: ")
        amount = input("Enter amount you would like to withdraw: ")
        mybank.withdrawal(pnr, acc_no, amount)
    elif inp == "9":
        pnr = input("Enter customers social security number: ")
        mybank.add_account(pnr)
    elif inp == "10":
        pnr = input("Enter customers social security number: ")
        acc_no = input("Enter account number from which you would like to see balance: ")
        print("\nAccount number: "+ mybank.get_account(pnr, acc_no).replace(", ", "\nAccount type: ", 1).replace(", ", "\nBalance: "))
    elif inp == "11":
        print("Good bye!")
        inp = False
    else:
        print("Please choose one of the menu options")