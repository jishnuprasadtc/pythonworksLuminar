from re import*
ph_num_rule="[\d]{10}"
gmail_rule="[a-z][\w\W]+[@]gmail[.]com"
mail=[]
ph=[]
f=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\regular expression\\data.txt")
for line in f:
    word=line.rstrip("\n").split(" ")
    for w in word:
         p_match=fullmatch(ph_num_rule,w)
         e_match=fullmatch(gmail_rule,w)
         if p_match!=None:
             ph.append(w)
         elif e_match!=None:
             mail.append(w)
print(ph)
print(mail)

# ***********************************************************************************





