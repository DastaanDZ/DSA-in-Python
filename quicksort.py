def quicksort(L,l,r):
    if (r-l<=1):
        return L
    (pivot,lower,upper) = (L[l],l+1,r+1)
    for i in range(l+1,r):
        if l[i]>pivot:
            upper = upper+1
        else:
            (l[i],L[lower]) = (L[lower],l[i])
        (L[l],L[lower -1]) = (L[lower -1],L[l])
        lower = lower-1
    quicksort(L,l,lower)
    quicksort(L,lower,upper)
    return L