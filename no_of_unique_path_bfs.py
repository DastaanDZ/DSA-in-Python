def BFS(Alist, end1, restrictednodes):
    visited,parent = {},{}
    for i in Alist.keys():
        visited[i] =False
        parent[i] = -1

    q = []
    visited[end1] = True
    q.append(end1)

    while len(q)>0:
        node = q.pop(0)
        for neighbour in Alist[node]:
            if not visited[neighbour] and neighbour not in restrictednodes:
                visited[neighbour] = True
                parent[neighbour] = node
                q.append(neighbour)

    return visited,parent

def findpath(parent,source,destination):
    node = parent[destination]
    path = []
    while node!=source:
        path.append(node)
        node = parent[node]
    return path


def backandforth(Alist,end1,end2):
    restrictednodes = []
    path_count=0
    visited,parent = BFS(Alist,end1,restrictednodes)
    while(visited[end2]):
        path_count +=1
        path = findpath(parent,end1,end2)
        restrictednodes.extend(path)
        visited,parent = BFS(Alist,end1,restrictednodes)

    return path_count