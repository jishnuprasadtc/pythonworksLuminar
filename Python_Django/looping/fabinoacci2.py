num=int(input("enter the value"))
currentvlu=1
previvlu=0
print(previvlu)
print(currentvlu)
for i in range(1,num+1):
    fabino=previvlu+currentvlu
    if(fabino<=num):
        print(fabino)
    previvlu=currentvlu
    currentvlu=fabino

