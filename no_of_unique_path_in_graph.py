def DFSInitList(AList):
    (visited,parent) = ({},{})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return (visited,parent)

def DFSList(AList,visited, parent, v,end):
    ans = False
    visited[v] = True
    if end in AList[v]:
        ans = True
        return (ans,visited,parent) 
    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            visited[k] = True
            (ans,visited,parent) = DFSList(AList,visited,parent,k,end)  
    return (ans,visited,parent)

def backandforth(Alist,start,end):
    countpath = 0
    visited,parent = DFSInitList(Alist)
    for i in Alist[start]:
        ans,visited,parent = DFSList(Alist,visited,parent,i,end)
        if ans:
            countpath += 1
    return countpath

end1 = int(input())
end2 = int(input())

AList = {}

while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)

print(backandforth(AList, end1, end2))