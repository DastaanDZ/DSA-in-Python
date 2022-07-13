def stringmatch(t,p):
    poslist = []
    for i in range(len(t)-len(p)+1):
        matched = True
        j=0
        while j<len(p) and matched:
            if t[i+j]!= p[j]:
                matched = False
            j+=1
        if matched:
            poslist.append(i)
    return(poslist)