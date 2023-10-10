from abc import ABC,abstractclassmethod

class Bike(ABC):

    @abstractclassmethod
    def starts(self):
        pass
    @abstractclassmethod

    def accelerate(self):
        pass
    @abstractclassmethod

    def stop(self):
        pass

class Intercepert(Bike):
    def starts(self):
        print("Intertceptor start")


    def accelerate(self):
        print("Intercepeter accelerate")  

    def stop(self):
        print("Interceptor Stop")  




obj =Intercepert()
obj.starts()
obj.accelerate()
obj.stop()



        