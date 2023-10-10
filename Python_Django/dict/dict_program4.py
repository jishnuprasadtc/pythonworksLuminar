text="carrot"
char={}
for ch in text:
    if ch in char:
        char[ch]+=1
    else:
        char[ch]=1
print(char)        
