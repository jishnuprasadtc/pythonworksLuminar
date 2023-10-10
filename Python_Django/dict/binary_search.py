lst=[12,2,4,15,16,18]
lst.sort()
element=2
low=0
upp=len(lst)-1
is_found=False
while(low<=upp):  #does over flow the low above the larger
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found=True
        break

    elif element<lst[mid]:
        upp=mid-1
    else:
        element>lst[mid]
        low=mid+1
print(is_found)        