# text="apple"
# for ch in text:
#     if ch in["a","e","i","o","u"]:
#         print(ch,"vowel")
#     else:
#         print("not")
text="Pneumonoultramicroscopicsilicovolcanoconiosis"
vowel_cnt=0
const_cnt=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
        vowel_cnt=vowel_cnt+1
    else:
        const_cnt=const_cnt+1
print("number of vowel",vowel_cnt)        
print("number of vowel",const_cnt)        
