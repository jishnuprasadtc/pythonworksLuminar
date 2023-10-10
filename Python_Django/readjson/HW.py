# print python frame work
from json import load
with open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\readjson\\data.json")as f:
    record=load(f)
# fw=[f.get("name") for f in record if f.get("language")=="python"]


# print python back end frame work
fw=[f.get("name") for f in record if f.get("side")=="backend"]
print(fw)




