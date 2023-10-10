# alpa
# number
# speacial
from re import*
g_mail=input("Enter the gmail:")
rule="[a-z\d][\W\w]+[@]gmail[.]com"
matchs=fullmatch(rule,g_mail)
print("invaild" if matchs==None else "valid")


# password 
# rule=one upper,1speacil,min 8 char