class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print("Link list: ", llstr)
        
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)
                
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def get_last_node(self):
        itr = self.head
        while itr.next: # While itr.next is not NULL
            itr = itr.next
        
        return itr
    
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1
                
                
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data) 



if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(4)
    dll.insert_at_beginning(6)
    dll.insert_at_beginning(54)
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(2, 43)
    dll.print_forward()
    dll.remove_at(1)
    dll.print_forward()
    
    dll.insert_values([3,4,5,7,25,24,266])
    dll.print_forward()