def merge(a,b):
    (m,n) = (len(a),len(b))
    (c,i,j,k) = ([],0,0,0)
    while(k< m+n):
        if i== m:
            c.extend(b[j:])
            k = k + (n-j)
        elif j==n :
            c.extend(a[i:])
            k = k + (n-i)
        elif a[i]<b[j]:
            c.append(a[i])
            (i,k) = (i+1,k+1)
        else:
            c.append(b[j])
            (j,k) = (j+1,k+1)
    return c

def mergesort(a):
    n = len(a)

    if n<=1:
        return a

    l = mergesort(a[:n//2])
    r = mergesort(a[n//2:])

    b = merge(l,r)
    return b
        
print(mergesort([[3,2],[1,5],[2,1],[1,4],[1,3],[1,2]]))   