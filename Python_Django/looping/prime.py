num=int(input("enter number to check prime or not:"))
isprime=True
for i in range(2,num):
    if(num%i==0):
        isprime=False
        break
print(isprime)    
