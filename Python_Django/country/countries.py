from json import load
path="C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\country\\countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)
# print(len(countries))



cntry_nm=[c.get("name") for c in countries]
# print(cntry_nm)

china_cptl=[c.get("capital") for c in countries if c.get("name")=="China"]
# print(china_cptl)

country_reg={c.get("region") for c in countries}
# print(country_reg)
cnty_br=[c.get("borders") for c in countries if c.get("name")=="India"][0]
# print(cnty_br)
border_nam=[c.get("name") for c in countries if c.get("alpha3Code")in cnty_br]
# print(border_nam)



# print idepent cnty name 

indpt_cntry=[c.get("name") for c in countries if c.get("independent")==True]
# print(indpt_cntry)
 
# print  name of indacurry
curre_name=[c.get("currencies")[0]for  c in countries  if c.get("name")=="India"]
# print(curre_name)



country_currenies=[c for c in countries if "currencies"in c]
currencies=[c.get("currencies")[0].get("symbol") for c in country_currenies]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
print(max( (v,k)for k,v in wc.items()))

no_curr=[nc.get("name") for nc in countries if "currencies" not in nc]
print(no_curr)