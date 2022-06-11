# Prefix Code
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()
            
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def isempty(self):
        if self.size == 0:
            return True
        return False

    def push(self,data):
        self.size+=1
        self.q2.enqueue(data)
        while self.q1.items!=[]:
            self.q2.enqueue(self.q1.dequeue())
        self.temp = self.q1
        self.q1 = self.q2
        self.q2 = self.temp

    def pop(self):
        if self.size !=0:
            self.size-=1
            return self.q1.dequeue()
        else:
            return('Stack is empty')

    def top(self):
        if not self.isempty():
            return self.q1.items[-1]
        else:
            return ('Stack is empty')
            

    



        
        
# Suffix Code
inp = eval(input())
dl = int(input())
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())

        
    