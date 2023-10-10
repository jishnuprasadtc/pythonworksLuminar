class Employee:   #class creating        SELF MUST IN ALL
    id:int  #defining
    name:str
    gender=str
    department=str
    slary=str
    
    def create(self,id,name,gender,dept,sal): #creating methods
        self.id=id
        self.name=name
        self.gender=gender
        self.department=dept
        self.slary=sal
        
    def get(self):  #print method
        print(self.id,self.name,self.gender,self.department,self.slary)


emp1=Employee()    #object creating
emp1.create(100,"raju","male","sales",100000)  #creating the object

emp2=Employee()
emp2.create(101,"rani","female","associate",12000)


emp1.get()   #object print 
emp2.get()
