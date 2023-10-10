# recursive word in text
text="abcdab"
wc={}
for ch in text:
    if ch in wc:
        print("the recurisive word is:",ch)
    else:
        wc[ch]=1


 #1st recurise  word
text="abcdab"
wc={}
for ch in text:
    if ch in wc:
        print("the recurisive word is:",ch)
        break
    else:
        wc[ch]=1     


