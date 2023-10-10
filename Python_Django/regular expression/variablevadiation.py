from re import*
variable=input("enter the variable:")
rule="[a-zA-Z][\w_]*"
matcher=fullmatch(rule,variable)
print("invaild"if matcher==None else "valid")


#rule
# k,,,,,m
# dight but divisible by 3
#any anynumber of chareter

