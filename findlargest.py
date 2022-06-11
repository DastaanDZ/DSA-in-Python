def findLargest(l):
    if len(l) == 1:
        return(l[0])
    mid = len(l)//2

    if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
        return(l[mid])
    if l[mid]<l[mid-1] and l[mid]<l[mid+1]:
        return(l[mid-1])
    if l[len(l)-1]>l[0]:
        return(l[len(l)-1])     
    if l[mid]>l[0]:
        return(findLargest(l[mid:]))
    elif l[mid]<l[0] and l[0]>l[len(l)-1]:
        return(findLargest(l[:mid]))
    
print(findLargest([5,6,1,2,3,4]))