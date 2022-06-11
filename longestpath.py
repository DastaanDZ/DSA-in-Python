def longestpathlist(Alist):
    (indegree,lpath) = ({},{})
    for u in Alist.keys():
        indegree[u] = 0
        lpath[u] = 0
    for u in Alist.keys():
        for v in Alist[u]:
            indegree[v] = indegree[v]+1

    zerodegreeq = Queue()
    for u in Alist.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)

    while( not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        indegree[j] = indegree[j]-1
        for k in Alist[j]:
            indegree[k] = indegree[k]-1
            lpath[k] = max(lpath[k], lpath[j]+1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)
            return