def binarysearch(v,l):
    if l == []:
        return False
    
    m = len(l)//2

    if v == l[m]:
        return True

    if v < l[m]:
        return binarysearch(v,l[:m])
    else:
        return binarysearch(v,l[m+1:])

v=0
print(binarysearch(v,[1,2,3,4,5,6,7,8,9]))