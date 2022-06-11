from queue import Queue


def BFSListPath(Alist,v):
    (visited,parent) = ({},{})
    for i in Alist.keys():
        visited[i] = False
        parent[i] = -1
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isEmpty():
        j = q.delq()
        for k in Alist[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)
    return (visited,parent)