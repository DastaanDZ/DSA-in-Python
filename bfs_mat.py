from queue import Queue


def BFS(AMat,v):
    (rows,cols) = AMat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isEmpty():
        j = q.deq()
        for k in neighbours(AMat,j):
            if not visited[k]:
                visited[k] = True
                q.addq(k)