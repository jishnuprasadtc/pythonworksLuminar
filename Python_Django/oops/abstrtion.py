# # # # abstration
# # # class Person: # manditory
# # #     def __init__(self):  #
# # #         self.name="jishnu"
# # #     def bio(self):
# # #         self.adr="abc"
# # #         self.course="xyxz"
# # # obj=Person()  # first check this 
# # # print(obj.name)
        
# # # ********************************************************************************************#


# # class Student:
# #     def __init__(self,name,course):
# #         self.name=name
# #         self.course=course
# #     def get_student(self):
# #         print("my name is ",self.name,"and my course is",self.course)

# # obj=Student("jishnu","python")
# # obj.get_student()
# # obj1=Student("prasad","react")
# # obj1.get_student()



# class Book:
#     def __init__(self) -> None:
#         self.id=int(input("enter the id:"))
#         self.name=(input("enter the title:"))
#         self.author=(input("enter the name of author:"))
#         self.price=int(input("the price:"))
#     def getauthor(self):
#         print(self.author)
#     def gettitle(self):
#         print(self.name)
#     def  setprice(self):
#         self.price=int(input("enter the price"))
#     def settitle(self) :
#         self.name=input("enter the title")
#     # def getdetails(self):
#     #     print(self.id)
#     #     print(self.name)
#     #     print(self.author)
#     #     print(self.price)   
# b1=Book()
# b1.getauthor()
# b1.gettitle()
# b1.setprice() 
# b1.settitle()
# # b1.getdetails()   
       

class Things:
    def mobile(self):
        print("vivo")
    def bike(self):
        print("dominar")
    def car(self):
        print("dodge")
class Child(Things):
    pass
c1=Child()
c1.bike()
c1.car()
c1.mobile()
        
    

