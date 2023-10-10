class Hotal:
    item=[ 

    {"id":100,"name":"cb","price":160},                                         # self is complesry
    {"id":101,"name":"vb","price":120},
    {"id":102,"name":"bb","price":180},
    {"id":103,"name":"mb","price":190},
    {"id":104,"name":"fb","price":110},
    {"id":105,"name":"pb","price":150}
    ]

# create
    def create(self,*args,**kwargs):
        self.item.append(kwargs)
        return f"{kwargs}created"


    def retrive(self,id=None,*args,**kwargs):
        obj=[i for i in self.item if i.get("id")==id][0]
        return obj
    

    def destory(self,id=None,*args,**kwargs):
        obj=[i for i in self.item if i.get("id")==id][0]
        self.item.remove(obj)
        return f"{obj}has been delete"
    
    def update(self,id=None,*args,**kwargs):
        obj=self.retrive(id=id)
        oldobj=obj.copy()
        obj.update(kwargs)
        return f"{oldobj} is updates{obj}"

    

    
obj=Hotal()
# print (obj.create(id=106,name="noodels",price=180))
# print(obj.retrive(id=102))
# print(obj.destory(id=103))
print(obj.update(id=102,name="BB",price=195))