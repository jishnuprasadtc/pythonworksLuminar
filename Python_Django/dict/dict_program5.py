# 1st covert to word using split method

text="hello hai hello hai" #split dute to space
word=text.split(" ")#intialing to the splited in to word bring the value of text to splited word
wr={}#assing all value into this empty dictionary
print(text)
for w in word:
    if w in wr:
        wr[w]+=1
    else:
        wr[w]=1
print(wr)        