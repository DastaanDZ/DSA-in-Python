def DFSInit(Amat):
    (rows,cols) = Amat.shape
    (visited,parent) = ({},{})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return (visited,parent)

def DFS(Amat,visited, parent, v):
    visited[v] = True
    for k in neighbours(Amat,v):
        if not visited[k]:
            parent[k] = v
            visited[k] = True
            (visited,parent) = DFS(Amat,visited,parent,k)

    return (visited,parent)