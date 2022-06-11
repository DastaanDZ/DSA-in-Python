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


def findIntersection(l1,l2):
    # print(l1,l2)
    l1.sort()
    l2.sort()
    a = []
    for i in range(len(l1)):
        if binarysearch(l1[i],l2):
            a.append(l1[i])
    return a


set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
result = findIntersection(set1, set2)
result.sort()
print(*result)