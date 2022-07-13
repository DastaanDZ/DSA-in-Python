from numpy import False_
from soupsieve import match


def boyermore(t,p):
    last = {}
    for i in range(len(p)):
        last[p[i]] = i

    poslist,i = [],0
    while i<= len(t)-len(p):
        matched,j = True,len(p)-1
        while j>=0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j-=1
        if matched:
            poslist.append(i)
            i+=1
        else:
            j+=1
            if t[i+j] in last.keys():
                i+=max(j-last[t[i+j]],1)
            else:
                i = i+j+1
    return(poslist)
            