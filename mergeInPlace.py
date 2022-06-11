# def merge(a,b):
#     (m,n) = (len(a),len(b))
#     (c,i,j,k) = ([],0,0,0)
#     while(k< m+n):
#         if i== m:
#             c.extend(b[j:])
#             k = k + (n-j)
#         elif j==n :
#             c.extend(a[i:])
#             k = k + (n-i)
#         elif a[i]<b[j]:
#             c.append(a[i])
#             (i,k) = (i+1,k+1)
#         else:
#             c.append(b[j])
#             (j,k) = (j+1,k+1)
#     return c

# def mergesort(a):
#     n = len(a)

#     if n<=1:
#         return a

#     l = mergesort(a[:n//2])
#     r = mergesort(a[n//2:])

#     b = merge(l,r)
#     return b

def mergeInPlace(a,b):
    for i in range(len(a)):
        if a[i]>b[0]:
            a[i],b[0] = b[0],a[i]
            b.sort()
    return(a,b)

print(mergeInPlace([2,4,6,9,13,15],[1,3,5,10]))