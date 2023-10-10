# find the 2nd recursive 
text="abcacd"
wc={}
dupli_lst=[]
for ch in text:
    if ch in wc:
        dupli_lst.append(ch)
    else:
        wc[ch]=1
print(dupli_lst)
#duplicate list print 



#2nd recurive
text="abcacd"
wc={}
dupli_lst=[]
for ch in text:
    if ch in wc:
        dupli_lst.append(ch)
    else:
        wc[ch]=1
print(dupli_lst[1])#here the index is given beacuse the the 0th is the 1st recusive
#but here we need the second so the 2nd is store in the intex 1 


# next method 

text="abastdba"
dup_lst=[]
non_duplst=[]
for ch in text:
    if ch in non_duplst:
        dup_lst.append(ch)
    else:
        non_duplst.append(ch)
print(dup_lst[1])        

