from abc import ABC,abstractclassmethod
class Bank(ABC):
    @abstractclassmethod
    def fundtransfer(self):
        pass
    @abstractclassmethod
    def balanceenqiry(self):
        pass
    @abstractclassmethod
    def transationhistory(self) :
        pass

       
class Gpay(Bank):
    def  fundtransfer(self):
        print("gpay transefer")

    def balanceenqiry(self):
        print("balance")   
    
    def transationhistory(self):
        print("history")
     

    def award(self):
        print("cash back")



obj=Gpay()
obj.balanceenqiry()
obj.fundtransfer()
obj.transationhistory()
obj.award()