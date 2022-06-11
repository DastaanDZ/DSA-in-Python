class LinkedList:

    def __init__(self):
        self.head = None
        return
    
    def reverse(self):
        prev = None
        current = self.head

        while(current!=None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

        