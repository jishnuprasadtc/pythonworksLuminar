

#  IF A LIST OF VARIABLE IS GIVEN AND THE QUESTION FOR CHECKING THE WE SHOULD APPLY THE FOR LOOP BECAUSE  ALL THE VAEIABLE SHOULD TAKE ONE BY ONE AND CHECK 
#  SHOULD ADD THE  AN EMETY VALUE FOR STORE THE NEW VALUE

orders=["vegmeals","fishmeals","vegmeals","fishmeals","cb","vb","bb","cb","bb"]
#use an empty for store the ordercount
order_count={}#defing a empty dict
for item in orders:  #take one by one
    if item in order_count:
        order_count[item]+=1
    else:
        order_count[item]=1
print(order_count)

