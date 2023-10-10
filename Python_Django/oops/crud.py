item=[ 

    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":120},
    {"id":102,"name":"bb","price":180},
    {"id":103,"name":"mb","price":190},
    {"id":104,"name":"fb","price":110},
    {"id":105,"name":"pb","price":150}
    ]


def add_items(*args,**kwargs):#function creting
    item.append(kwargs)

add_items(id=106,name="bb",price=50)
# print(item)




def retrive_item(id=None,*args,**kwargs):
     obj=[r for r in item if r.get("id")==id]
     return obj

# print(retrive_item(id=100))




def destory_item(id=None,*args,**kwargs):
     obj=[r for r in item if r .get("id")==id][0]
     item.remove(obj)

destory_item(id=102)
# print(item)



def update(id=None,*args,**kwargs):
     obj=[r for r in item if r.get("id")==id][0]
     obj.update(kwargs)

update(id=104,name="gee rice",price=80 )
# print(item)
     



print(retrive_item (id=100))