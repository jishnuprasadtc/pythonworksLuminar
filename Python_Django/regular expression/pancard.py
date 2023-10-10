# A-Z
# [4th plc pcfhta]
# random upper case
# 4 digit
# one apl
from re import*
pan_card=input("enter the pancard number:")
rule="[A-Z]{3}[PCFHTA][A-Z][\d]{4}[A-Z]"
matchs=fullmatch(rule,pan_card)
print("invalid" if matchs==None else "valid")


