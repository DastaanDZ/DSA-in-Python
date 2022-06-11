def checkequal(l):
    eql = l[0]
    for i in range(len(l)):
        if l[i]!=eql:
            return True
    return False

def equalafter(l):
    count=0
    k=1
    while(checkequal(l)):
        if k>len(l):
            k = len(l)-1
        print(l)
        temp1 = l[k-1]
        temp2 = l[k]

        if temp1&temp2 == l[k] and temp1&temp2 == l[k-1]:
            count = count
        else:
            l.remove(l[k-1])
            l.remove(l[k-1])
            print(l)
            l.insert(k-1,temp1&temp2)
            count+=1
            print(l)
        k+=1    
    return count
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(equalafter(l))    