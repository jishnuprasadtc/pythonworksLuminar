# print all vowels
from re import*
text="goodmoring #sachin"
# pattern="[aeiou]"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group()) 
