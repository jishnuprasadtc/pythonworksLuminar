v=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\file_input_output opreation\\vehinumber.txt")
all_number=[line.rstrip("\n") for line in v]
print(all_number)
ker_num=[num for num in all_number if num.startswith("kl")]
print(ker_num)