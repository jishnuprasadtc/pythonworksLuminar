num1=int(input("enter the first:"))
num2=int(input("enter the second:"))
num3=int(input("enter the third:"))
def largest(num1,num2,num3):
    if(num1>num2) and (num1>num3):
        print("first is larger",num1)
    elif(num2>num1)and (num2>num3):
        print("second is larest",num2)
    else:
        print("third is largest",num3)
largest(num1,num2,num3)          


