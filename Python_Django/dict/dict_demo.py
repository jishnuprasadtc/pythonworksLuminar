# key : value  repeat to entire data enter
# key  is main
mobile={"name":"poco","brand":"mi","colour":"blue","price":10000}#initi using the dict 
print(mobile["colour"]) #calling the  dict



# adding the new value.
# syntax: dict_obj[key]=value
mobile["display"]="amoled"
print(mobile)


# checking a key in dict
#syntax: if key in dict_obj

if "offer" in mobile:  #checking using the membership operator"in"
    print("offer key is present")
else:
    print("offer key is not present")

