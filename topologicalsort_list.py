def toposortList(Alist):
    (indegree,toposortlist) = ({},[])
    for u in Alist.keys():
        indegree[u]=0
    for u in Alist.keys():
        for v in Alist[u]:
            indegree[v] += 1

    zerodegreeq = []
    for u in Alist.keys():
        if indegree[u] == 0:
            zerodegreeq.append(u)

    while (not zerodegreeq.isempty()):
        j = zerodegreeq.pop()
        toposortlist.append(j)
        for k in Alist[j]:
            indegree[k] -= 1
            if indegree[k] == 0:
                zerodegreeq.addq(k)
