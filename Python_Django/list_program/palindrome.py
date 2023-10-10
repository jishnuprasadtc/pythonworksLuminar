
text="malayalam"
count=len(text)-1
srt=""# 
for i in range(count,-1,-1):
    srt=srt+text[i]
if text==srt:
    print("palindrome")
else:
    print("not a palindrome")   
    