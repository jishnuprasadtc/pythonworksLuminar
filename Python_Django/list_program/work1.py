
# #arr=[1,3,4,6,5,] find the missig         LIST IS MAIN
# arr=[1,2,3,10,5,6]
# arr.sort()
# if arr[0]!=1:
#     print("1 is missing ")
# else:

# # arr=[1,3,4,6,5]
# # # arr.sort()
# #     for i in range(0,len(arr)-1):
# #         current=arr[i]
# #         nxt=arr[i+1]
# #         if nxt-current!=1:
# #             print(current+1,"is missing")
# #             break



# # # 2 PAIR SUM  (use "while" we don't know the exact destination)
# lst=[1,2,3,4,5,6]
# sum=7
# lower=0
# upper=len(lst)-1
# # initialising
# while(lower<upper):#condition  if the destination is not  given 
#     currentsum=lst[lower]+lst[upper]
#     if (currentsum==sum):#condtion checking
#         print(lst[lower],lst[upper])
#         break
#     elif(currentsum<sum):
#         lower=lower+1
#     else:
#         upper=upper-1
    
  
                                                                    
lst1=[1,3,5,7]
lst2=[5,6,8,9]
# for e in lst1: for taking one by one  
#     if e in lst2:
#         print(e)

# for n in lst1:
#     for j in lst2:
#         if n==j:
#             print(j)

lst1.sort()
lst2.sort()
p1,p2=0,0 #giving index postion
while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print("common",lst2[p2])
      
        p2+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    else:
        p2+=1        