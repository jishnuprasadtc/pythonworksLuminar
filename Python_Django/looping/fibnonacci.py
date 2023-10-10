prev=0
cur=1
start=1
print(prev)
print(cur)
while(start<=9):
    fib=prev+cur
    print(fib)
    prev=cur          #continue
    cur=fib
    start=start+1