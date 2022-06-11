def siei(n,l):
    if (l.index(n)-l.index(l[0])+1)>=n:
        si = l.index(n)-n+1
    else:
        si = l.index(l[0])
    if (l.index(n)+n-1)>=0:
        ei = l.index(n)+n-1
    else:
        ei = len(l)-1
    return(si,ei)    

def subarray(l):
    for num in l:
        si,ei = siei(num,l)
        

            


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    subarray(a)