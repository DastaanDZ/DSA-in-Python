(visited,pre,post) = ({},{},{})

def DFSInitPrePost(Alist):
    for i in range(len(Alist)):
        visited[i] = False
        pre[i] = -1
        post[i] = -1
    return

def DFSPrePost(Alist,v,count):
    visited[v] = True
    pre[v] = count
    count += 1
    for k in Alist[v]:
        if not visited[k]:
            count = DFSPrePost(Alist,k,count)
    post[v] = count
    count += 1
    return count