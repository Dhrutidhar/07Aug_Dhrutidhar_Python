import random

class welcome:
    acc_no = 100
    acc_name = ''
    acc_type = ''
    def account_details(self):
        self.acc_no = random.randint(100, 999)
        self.acc_name = input("Enter Account Holder name: ")
        self.acc_type = input("Enter Account Type: ")

class deposite_withdrawl(welcome):
    bal = 0
    def deposite(self): 
        self.dep = int(input("Enter the Amount you have to Deposite: "))
        self.bal = self.bal +  self.dep
        print("YOu have Deposited: ", self.dep)

    def withdrawl(self):
        self.wit = int(input("Enter the Amount you have to Withdraw: "))
        self.bal = self.bal -  self.wit   
        print("Remaing amount is: ", self.wit)
    

class passbook(deposite_withdrawl):
    def statement(self):
        print("------------Your Account Detail ---------------")
        print("\tAccount Number: ", self.acc_no)
        print("\tAccount Name: ", self.acc_name)
        print("\tAccount Type: ", self.acc_type)
        print("\tAcoount Remaning Amount: ", self.bal)
       

ma = passbook()
ma.account_details()
ma.deposite()
ma.withdrawl()
ma.statement()

