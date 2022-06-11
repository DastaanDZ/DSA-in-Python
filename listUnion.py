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

def listUnion(list1, list2):
    print(list1)
    print(list2)
    """
    This function takes two lists and returns a list of all the elements that are in both lists.
    """
    list3 = []

    list3 = list1 + list2

    for i in list1:
        if binarysearch(i, list2):
            print(i,end='\n')
            list3.remove(i)
    list3.sort()
    print('LIST3')
    print(list3)

    return list3

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*listUnion(set1, set2))