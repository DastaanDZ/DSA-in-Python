def printl(l):
    for i in range(len(l)):
        print(l[i],end = ' ')

def equaldiff(n,l):
    # print(n,l)
    if len(l)<=2:
        printl(l)
    else:
        unique = []
        for i in range(len(l)):
            if [l.count(l[i]),l[i]] not in unique:
                unique.append([l.count(l[i]),l[i]])
        # print(unique)
        unique.sort(reverse = True)
        # print(unique)
        print('ans',len(l)-l.count(unique[0][1]))
        print('Done')
    
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    equaldiff(n,l)