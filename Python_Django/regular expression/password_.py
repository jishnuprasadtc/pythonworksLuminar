from re import*
psw=input("enter the password:")
code="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}" #for not check the cursor run ith should be any wher
matchs=fullmatch(code,psw)
print("notvalid"if matchs==None else "valid")





# ?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}
# (?=.*[A_Z])(?=.*[\W](?+.*[\d]).{8,}