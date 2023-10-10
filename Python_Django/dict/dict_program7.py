# counting  is must
text="abbccdef"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for v,k in wc.items(): #"v" for storing the value & "k" for store the  key value
    if k==1:
        print(v)
    