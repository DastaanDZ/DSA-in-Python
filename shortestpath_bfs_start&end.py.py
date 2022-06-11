def BFS(Alist,start):
    level = {}
    parent = {}
    for i in Alist.keys():
        level[i] = -1
        parent[i] = -1
    q = []
    level[start] = 0
    q.append(start)
    while len(q)>0:
        item = q.pop(0)
        for k in Alist[item]:
            if level[k] == -1:
                level[k] = level[item]+1
                parent[k] = item
                q.append(k)
    return level,parent

def minimumhops(Alist,start,end):
    level,path = BFS(Alist,start)
    spath = []
    if level[end]!=-1:
        spath.append(end)
        while spath[-1]!= start:
            end = path[end]
            spath.append(end)
        spath.reverse()
        return spath
    else:
        return spath.append(start)
