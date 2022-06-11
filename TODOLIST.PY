def removeList(n,l):
    i=0
    while(i<len(l)):
        if l[i]>=1000:
            l.remove(l[i])
            i = i-1
        i+=1
    return(n-len(l))


t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(removeList(n,l))