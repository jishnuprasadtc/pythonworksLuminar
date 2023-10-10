mobile={"name":"poco","brand":"mi","colour":"blue","price":10000,"offer":100}  #dict
if "offer" in mobile:#checking that the offer in mobile dicitionatry
    mobile["offer"]+=50 #add the additionl 50 to the existing offer
else:
    mobile["offer"]=50 #else just print the offer is 50
print(mobile)




