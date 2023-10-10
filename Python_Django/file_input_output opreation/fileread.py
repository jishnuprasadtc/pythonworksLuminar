#syntax== variable=open("__path__","opreation")
#take loop for taking one by one
f=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\file_input_output opreation\\data.txt","r")
word=[line.rstrip("\n") for line in f]
print(word)


