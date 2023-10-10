# properties
# duplication not allowed
# update allowed
# insertion not preserved
# mutable


# st=set()#for declaring emty set

stt={10,20,11,12} #declaring the set
stt1={20,21,11,30,40}
# add
stt.add(200)
print(stt)


# uninon
unionset=stt.union(stt1)
print(unionset)


# intersection of set
intersetion=stt.intersection(stt1)
print(intersetion)

# diffence
differeceset=stt.difference(stt1)
print(differeceset)

# remove an element
stt.remove(10)
print(stt)

# *********************************************************************
#if exsist it will remove or noting will happen
stt.discard(20) 
print(stt)


#remove random object
stt.pop()
print(stt)

# symmertic difference
st1={4,5,6,7}
st2={6,7,8,9}
symmertic=st1.symmetric_difference(st2)
print(symmertic)



