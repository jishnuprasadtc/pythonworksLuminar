year=[ y for y in range(1800,2024)]
print(year)


#centuey 

century_year=[y  for y in year if y %100==0]
print(century_year)

#non century
print("**************")
non_century_years=[y for y in year if y %100!=0]
print(non_century_years)

