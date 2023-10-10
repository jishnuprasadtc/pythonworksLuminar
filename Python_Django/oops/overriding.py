class Car:
    def key_start(self):
        print("key start")
    def break_system(self):
        print("drum break")
    def transmission(self):
        print("mannual")

class Marathi800(Car):
                        #  overriding program
    def key_start(self):
        print("self _start")
    def break_system(self):
        print("disc braking")
    def transmission(self):
        print("automatic")
    

obj=Car()
obj.key_start()
obj.break_system()
obj.transmission()





print("******************Marathicar****************")


obj1=Marathi800()
obj1.key_start()
obj1.break_system()
obj1.transmission()