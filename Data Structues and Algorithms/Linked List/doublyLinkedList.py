class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
class doublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return
        
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data)
            itr = itr.next


if __name__ == "__main__":
    dll = doublyLinkedList
    dll.insert_at_beginning(3)
    dll.print()
