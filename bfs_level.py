def BFSListPathLevel(AList,v):
    (level,parent) = ({},{})
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = Queue()

    level[v] = 0
    q.addq(v)

    while not q.isEmpty():
        j = q.delq()
        for k in AList[j]:
            if level[k]==-1:
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)
    return (level,parent)