class Book:
    book_name=str
    authore=str
    price=int
    page=int

    def __init__(self,bname,author,price,page):
        self.book_name=bname
        self.authore=author
        self.price=price
        self.page=page
                                                                
    def get(self): #print
        print(self.book_name,self.authore,self.price,self.page)   

    def __str__(self) -> str: #string representation 
        return(self.book_name + str(self.price))
        
    
obj=Book("aadujeevitham","benyamin",200,1000)
obj.get()
obj1=Book("aarachar","meera",195,1000)
obj1.get()

print(obj)
print(obj1)      
        