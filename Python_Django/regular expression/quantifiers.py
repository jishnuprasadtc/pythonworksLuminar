from re  import*
text="aabbaaac"
# pattern="a+"[ one or more occurence]
# pattern="a*"
pattern="a{1,2}"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())