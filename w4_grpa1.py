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

def findConnectionLevel(vertices, Amat, x,y):
    visited = {}
    level = {}
    for i in range(0,vertices):
        visited[i] = False
        level[i] = -1
    # print('visited:',visited)
    # print('level:',level)

    q = Queue()

    visited[x] = True
    level[x] = 0

    # print('visited:',visited)
    # print('level:',level)

    q.addq(x)

    # print('q:',q)

    while(visited[y]!=True):
        j = q.delq()
        if j==None:
            return 0
        # print('j:',j)
        # print('q:',q)
        for k in range(len(Amat[j])):
            print('k:',k)
            if Amat[j][k]==1 and not visited[k]:
                visited[k] = True
                level[k] = level[j] + 1
                q.addq(k)
                # print('q:',q)
    return level[y]




vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))