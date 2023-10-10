# sourceword="chicken"
# targetword="hen"
# sourcelst=[]
# kangaroo=""
# for ch in sourceword: 
#     sourcelst.append(ch) #add the source in to sorce list one by one
# for ch in targetword:
#     if ch in sourcelst: #check the source list which the target word present
#         sourcelst.pop(sourcelst.index(ch)) #remove the target word from the source list if it exist
#         kangaroo+=ch   #add the ch in to kangaroo word
# if kangaroo==targetword:
#     print("kangaroo word")
# else:
#     print("not")


 
#using dictionary

sourcewords="chicken"
target_word="hen"
flag=True
wc={}
for ch in sourcewords:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        flag=False
        break
print("kangaroo word" if flag==True else "not kangaroo")

