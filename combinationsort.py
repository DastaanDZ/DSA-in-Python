def insertionsort(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        j=i
        while(j>0 and l[j][0]<l[j-1][0]):
            (l[j],l[j-1]) = (l[j-1],l[j])
            j=j-1
    return l

def insertionsort1(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        j=i
        while(j>0 and int(l[j][1:])<int(l[j-1][1:])):
            (l[j],l[j-1]) = (l[j-1],l[j])
            j=j-1
    return l


def sort(l):
    n = len(l)
    l1 = []
    final = []
    temp  = l[0][0]
    for i in range(n):
        if l[i][0] == temp:
            l1.append(l[i])
    
        else:
            l1 = insertionsort1(l1)
            print(l1)
            final.extend(l1)
            temp = l[i][0]
            l1 = []
            l1.append(l[i])
    l1 = insertionsort1(l1)
    final.extend(l1)
    print(final)

def converttostrings(l):
    str1 = ''
    for i in range(len(l)):
        if i<len(l)-1:
            str1 = str1 + l[i]+','
        else:
            str1 = str1 + l[i]
    return str1

def combinationsort(l):
    n = len(l)
    l1 = insertionsort(l)
    str1  = converttostrings(l1)

    l2 = sort(l)
    str2  = converttostrings(l2)
    print('L1:',str1)
    print('L2:',str2)


combinationsort(input().split(', '))