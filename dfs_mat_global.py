(visited,parent) = ({},{})

def DFSInitGlobal(Amat):
    (rows,cols) = Amat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return

def DFSGlobal(Amat,v):
    visited[v] = True
    for k in neighbours(Amat,v):
        if not visited[k]:
            parent[k] = v
            visited[k] = True
            DFSGlobal(Amat,k)
    return