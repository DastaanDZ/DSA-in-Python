def toposort(Amat):
    (rows,cols) = Amat.shape
    indegree = {}
    toposortlist = []

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if Amat[r,c] == 1:
                indegree[c] += 1
    
    for i in range(rows):
        j = min([k for k in range(cols)
            if indegree[k] == 0])
        toposortlist.append(j)
        indegree[j] = indegree[j] -1
        for k in range(cols):
            if Amat[j,k] == 1:
                indegree[k] -= 1
    return toposortlist