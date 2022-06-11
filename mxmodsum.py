def mxmodsum(n,m,l):
    count = []
    if len(l)<=2:
        for i in range(n):
            for j in range(n):
                if l[i]-l[j]<0:
                    count.append(l[i]+l[j]+(m-abs(l[i]-l[j])))
                else:
                    count.append(l[i]+l[j]+((l[i]-l[j])%m))
        return(max(count))
    l.sort()
    if l[len(l)-1]+l[len(l)-2]>m:
        return(l[len(l)-1]+l[len(l)-2]+abs(l[len(l)-1]-l[len(l)-2])%m)
    else:
        return(l[0]+l[1]+abs(l[0]-l[1])%m)
t = int(input())
for i in range(t):
    n,m= list(map(int, input().split()))
    l= list(map(int, input().split()))
    print(mxmodsum(n,m,l))# cook your dish here
