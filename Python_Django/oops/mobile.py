mobile=[
    {"name":"poco","brand":"redmi","os":"Android" },
    {"name":"x3","brand":"redmi","os":"Android" },
    {"name":"iphonex","brand":"iphone","os":"ios" },
    {"name":"galaxy","brand":"samsung","os":"Android" }
]


def add_new(*args,**kwargs):
    mobile.append(kwargs)

add_new(name="edge",brand="motorola",os="Android")
# print(mobile)



def retrive(name=None,*args,**kwarge):
    obj=[m for m in mobile if m.get("name")==name]
    return obj

# print(retrive("poco"))


def update(name=None,*args,**kwargs):
    obj=[m for m in mobile if m.get("name")==name][0]
    obj.update(kwargs)
   

update(name="x3",brand="mi")
# print(mobile)



def delete(name=None,*args,**kwargs):
    obj=[m for m in mobile if m.get("name")==name][0]
    mobile.remove(obj)


delete(name="x3")
print(mobile)







