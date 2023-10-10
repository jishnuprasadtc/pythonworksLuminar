# num=321
# sum=0
# while(num!=0):
#     digit=num%10
#     sum=sum+digit
#     cube=sum**3 
#     num=num//10
# print(cube)
 
  
# num=371
# sum=0
# while(num!=0):
#     digit=num%10
#     cube=digit**3
#     sum=sum+cube
#     num=num//10
# print(sum)

num=int(input("enter the number:"))
orginal=num            #store the amstrong value
sum=0
while(num!=0):
    dight=num%10
    cube=dight**3
    sum=sum+cube
    num=num//10  #take single digit 
print(sum)    
if(sum==orginal):
    print("amstrong")
else:
    print("not amstrong")









