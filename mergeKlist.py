import numpy as np

def mergeKLists(l):
    length = len(l)
    minl = []
    while(l.count([])!=length):
        minval= np.inf
        popi = -1
        for i in range(length):
            if l[i]!=[] and l[i][0]<minval:
                minval = l[i][0]
                popi = i
            l[popi].pop(0)
        minl.append(minval)
    return(minl)
# k = int(input())
# LL=[]
# for i in range(k):
#     subL = [int(item) for item in input().split(" ")]
#     LL.append(subL)
LL = [[4,5],[8,26,69]]
print(*mergeKLists(LL))