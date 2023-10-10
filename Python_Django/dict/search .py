# linear search
lst=[15,16,18,17,20]
element=16
i=0
stop=len(lst)
is_found=False
while i<stop:
    currentvalue=lst[1]
    if currentvalue==element:
        is_found=True
        break
    i=i+1
print(is_found)