# 3digit
# /
# 2digitR [R] only if need this only
# 2dight
# /
# 2dighit 1 aph

from re import*
vehicle_tyre=input("Enter the tyre number:")
rule="[\d]{3} [/] [\d]{2}[R]\d{2}"
matchs=fullmatch(rule,vehicle_tyre)
print("invalid"if matchs==None else "valid" )