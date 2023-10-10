#SYNTAX=  VARIABLE NAME=[RETURN FOR LOOP CONDITION]


lst=[4,5,6,7,8,2,1]
squre=[n**2 for n in lst]
print(squre)


# cube
cube=[n**3 for n in lst]
print(cube)



even=[n for n in lst if n%2==0]
print(even)


odd=[ n for n in lst if n%2!=0]
print(odd)


num_gtfive=[n for n in lst if n>=5]
print(num_gtfive)
