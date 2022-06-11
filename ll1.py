class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getCount(head):
        temp = head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

def getNthNodeFromEnd(head, n):
    dummy = head
    for i in range(getCount(dummy)-n):
        dummy = dummy.next
    return dummy.data