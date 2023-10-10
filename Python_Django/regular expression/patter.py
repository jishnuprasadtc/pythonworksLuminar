from re import*
txt="Python @123"
# pattern="[a-z]"
# pattern="[A-Z]"
# pattern="[0-9]"
# pattern="\d"
# pattern="\D"
# pattern="\w"#speacial charater avoid
pattern="\W" 
# pattern="[a-zA-Z]"
# pattern="[a-z0-9A-Z]"
# pattern="[^a-zA-Z0-9]"           #^charater symbol for excuding 
matcher=finditer(pattern,txt)
for m in matcher:
    print(m.start(),m.group())

