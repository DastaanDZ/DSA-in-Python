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

def findPair(l,n):
    l.sort()
    for i in range(n):
        diff = n-l[i]
        if binarysearch(diff,l):
            return True
    return False


L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))