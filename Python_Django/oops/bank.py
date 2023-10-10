class Bank:
    Ac_no:int
    person_name:str
    ifsc_code:int
    branch:str
    ac_type:str
    balance:int
    bank_name:str


    def create(self,acnumber,personname,ifsccode,branch,actype,balance,bankname):
        self.Ac_no=acnumber
        self.person_name=personname
        self.ifsc_code=ifsccode
        self.branch=branch
        self.ac_type=actype
        self.balance=balance
        self.bank_name=bankname


    def deposit(self,amount):
        self.balance+=amount
        print(f"your balance  {self.bank_name} account has been credited {amount} avalable balance is {self.balance}")
    
    def withdrawl(self,amount):
        if amount>self.balance:
            print("insufficent balance")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} is debited with {amount} balance amount is {self.balance}")



    def get_balance(self):
       print(f"your balance is {self.balance}")

acc1=Bank()
acc1.create(20202,"raju",58976431,"kannur","savings",100000,"sbi")
acc1.deposit(1000)
acc1.withdrawl(5)
acc1.get_balance()