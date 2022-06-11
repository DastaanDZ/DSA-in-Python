def DFSInitList(AList):
    (visited,parent) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return (visited,parent)

def DFSList(AList,visited, parent, v):
    visited[v] = True
    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            visited[k] = True
            (visited,parent) = DFSList(AList,visited,parent,k)

    return (visited,parent)