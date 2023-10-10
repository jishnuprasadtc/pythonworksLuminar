from re import*
phone=input("enter the number:")
rule="\d{10}"
matcher=fullmatch(rule,phone)
if matcher==None:
    print("not valid")
else:
    print("valid")