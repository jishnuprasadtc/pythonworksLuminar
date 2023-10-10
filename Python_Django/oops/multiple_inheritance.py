class  P1:
    def m1(self):
        print("inside class P1M1 method")

class P2:
    def m2(self):
        print("inside class P2m2 method")
    
class Child(P1,P2):
    def m3(self):
         print("inside class P3m3 method")

obj=Child()
obj.m1()
obj.m2()   #object callig
obj.m3()
