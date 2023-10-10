class Parent:
    phone="Iphone"
    bike="interceptor"
    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class Child(Parent):
    pass
obj=Child()
obj.mobile()
obj1=Child()
obj1.vehicle()