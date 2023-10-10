# add=lambda n1,n2:n1+n2
# sub=lambda n1,n2:n1-n2
# cub=lambda n1:n1**3
# squre=lambda n:n**2
# maxtwo=lambda n1,n2:n1 if n1>n2 else n2
# min_two= lambda n1,n2:n1 if n1<n2 else n2
# print(add(10,20))#1
# print(sub(10,20))#2
# print(cub(3))#3
# print(maxtwo(10,20))#4
# print(min_two(15,30))#5
# print(squre(10))#6
# key is used for differnet implimentaion rather than default
# without the key it use ascci nethod
text= "hi hello hai goodafternoon"
word=text.split(" ")
l_word=max(word,key=lambda w:len(w))  #this method is use for removing the default method like asci
print(l_word)


srt=sorted(word,reverse=True,key=lambda w: len (w))
print(srt)