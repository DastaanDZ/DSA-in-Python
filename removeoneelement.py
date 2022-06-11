def checkwitha(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] in b:
            count+=1
    
    if count == len(b):
        return True
    else:
        return False

def removeOne(a,b):
    match = False
    x=1
    while(match!=True):
        for i in range(len(b)):
            b[i] = b[i] - x

        print(b)
        x+=1
        if checkwitha(a,b):
            match = True
    return(x)

t = int(input())
for i in range(t):
    n = int(input())
    (a,b) = (list(map(int, input().split())),list(map(int, input().split())))
    removeOne(a,b)