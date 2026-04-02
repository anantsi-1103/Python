import os
from abc import ABC,abstractmethod

# abstract class (Abstraction)
class Account:
    def __init__(self, accountnumber , owner , balance = 0):
        self.accountnumber = accountnumber
        self.owner = owner
        self.__balance = balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            # self.__balance = self.__balance + amount
            print(f"Deposited {amount}, New Balance : {self.__balance}")
        else:
            print("Invalid Deposit Amount")

    def getBalance(self):
        return self.__balance

    def setBalance(self, new_balance):
        self.__balance = new_balance

    # dunder function
    def __str__(self):
        return f"Account [{self.accountnumber}] - Owner : {self.owner}, Balance : {self.__balance}"

# inheritance + Polymorphism
class SavingsAccount(Account):
    def withdraw(self, amount): #1000
       if(amount <= self.getBalance()): # 2000
          self.setBalance(self.getBalance() - amount)
          print(f'Withdraw Amount {amount} , Closing Balance : {self.getBalance()}')
       else:
           print(f"Insufficient Balance in your Account")

class CurrentAccount(Account):
    def __init__(self, accountnumber, owner, balance=0, od_limit = 10000):
        # account class ke init se mil rha hai
        super().__init__(accountnumber, owner, balance)

        #current account individual assign krdiya 
        self.od_limit = od_limit


    def withdraw(self, amount):
       # 2000 <= 5000 + 10000
       if(amount <= self.getBalance()+ self.od_limit):
           self.setBalance(self.getBalance() - amount)  
           print(f'Withdraw Amount {amount} , Closing Balance : {self.getBalance()}')
       else:
           print(f"Insufficient Balance + OD limit Exceeded in your Current Account")

class Customer:
    def __init__(self , name , custID):
        self.name = name
        self.custID = custID


    def __str__(self):
     return f"Customer name : {self.name} - Customer ID : {self.custID} "
    
class Bank:
    def __init__(self , fileName= "project/accounts.txt"):
        self.accounts = {}
        self.filename = fileName
        self.load_account()


    def createAccount(self, Account_type , account_number , owner):
        if Account_type == "savings":
            account = SavingsAccount(account_number, owner)
        elif Account_type == "current":
            account = CurrentAccount(account_number, owner)
        else:
            print("Invalid Type")
            return
        
        self.accounts[account_number] = account
        self.saveAccounts()
        print(f"{Account_type.capitalize()} account created for {owner.name}")


    def getAccount(self,  account_number):
        return self.accounts.get(account_number)
    


    def saveAccounts(self):
        with open (self.filename , "w" ) as f:
            for acc in self.accounts.values():
                # dict -> collection ka data us colleciton ke class ka naam
                acc_type = acc.__class__.__name__
                f.write(f"{acc_type}, {acc.accountnumber}, {acc.owner.name},{acc.owner.custID},{acc.getBalance()}\n")

    def load_account(self):
        if not os.path.exists(self.filename):
            return 
        
        with open(self.filename, "r") as f:
            for line in f:
                acc_type , acc_no, name ,custID, balance = line.strip().split(",")
                owner = Customer(name , int(custID))

                if acc_type == "SavingsAccount":
                    acc = SavingsAccount(int(acc_no) , owner, float(balance))

                else:
                    acc = CurrentAccount(int(acc_no) , owner, float(balance))

                self.accounts[int(acc_no)] = acc


# starter -> engine 
if __name__ == "__main__":
    bank = Bank()


    while(True):
        print("\n ------ Bank Menu -----")
        print("1. Create Saving Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")


        choice = int(input("Enter your Choice : "))

        if(choice == 1):
            name = input("Enter your Customer Name : ")
            cID = int(input("Enter your Customer ID : "))
            acc_no = int(input("Enter your Account Number: "))
            bank.createAccount("savings" , acc_no, Customer(name , cID))

        elif(choice == 2):
            name = input("Enter your Customer Name : ")
            cID = int(input("Enter your Customer ID : "))
            acc_no = int(input("Enter your Account Number: "))
            bank.createAccount("current" , acc_no, Customer(name , cID))


        elif(choice == 3):
            acc_no = int(input("Enter your Account Number: "))
            amount = float(input("Enter your Deposit Amount : "))
            acc = bank.getAccount(acc_no)

            if acc:
                acc.deposit(amount)
                bank.saveAccounts()
            else:
                print("Account Not Found")


        elif(choice == 4):
            acc_no = int(input("Enter your Account Number: "))
            amount = float(input("Enter your Deposit Amount : "))
            acc = bank.getAccount(acc_no)

            if acc:
                acc.withdraw(amount)
                bank.saveAccounts()
            else:
                print("Account Not Found")

        elif(choice == 5):
            acc_no = int(input("Enter your Account Number: "))
            acc = bank.getAccount(acc_no)

            if acc:
                print(f'Balance for Your Account number : {acc_no} = {acc.getBalance()}')
            else:
                print("Account Not Found")

        elif(choice == 6):
            print("Exit--- Thank for using Us!!!")
            break

        else:
            print("Invalid Choice!!! Please try Again!!!!")
