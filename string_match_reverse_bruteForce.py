def stringmatch(t,p):
    poslist = []
    for i in range(len(t)-len(p)+1):
        matched = True
        j= len(p)-1
        while j>=0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j-=1
        if matched:
            poslist.append(i)
        return(poslist)
        