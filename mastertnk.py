class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v

    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return str(self.queue)

def bfs(Alist,v):
    countm=0
    visited = {}
    for i in Alist.keys():
        # print('key',i)
        visited[i] = False
    q = Queue()
    
    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in Alist[j]:
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    for i in visited.keys():
        if visited[i] == True:
            countm+=1
    if countm == len(visited):
        return(v)
    return -1
def findMasterTank(v,e):
    Alist = {}
# In dictionay AList, for example, AList[i] = [j,k] represent two edge from i to j and i to k
    for i in v:
        Alist[i] = []
    for (i,j) in e:
        Alist[i].append(j)

    # print(Alist)
    for i in Alist.keys():
        c = bfs(Alist,i)
        if c != -1:
            return c


v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))