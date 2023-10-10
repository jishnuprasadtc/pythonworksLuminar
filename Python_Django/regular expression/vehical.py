from re import*
# start with KL     kl 59 u 1969
# (kl) should first [EITHER K OR L  IF WE GIVEN [KL]]
# 2 digit
# 2 alph
# 4 digit



vehicle_num=input("Enter the vehicle number:")
rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"
mtch=fullmatch(rule,vehicle_num)
print("invaild" if mtch==None else "valid")


