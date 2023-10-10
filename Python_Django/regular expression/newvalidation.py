from re import*

variable=input("enter the number:")
rule="[k-m][369][\w]*"

matchs=fullmatch(rule,variable)
print("invalid"if matchs==None else "valid")
