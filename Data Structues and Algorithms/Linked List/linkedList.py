class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
                        
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1: # Stop at previous element to modify the next link
                node = Node(data, itr.next)
                itr.next = node
                break
                
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)            
                break
            
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next
        
    def print(self):
        if self.head is None:   
            print("Linked list is empty")
            return
        
        itr = self.head # iterator = head of current link
        llstr = ''
        while itr: # while iterator ! NULL
            llstr += str(itr.data) + '-->'
            itr = itr.next  # follow the link down the list
        
        print(llstr)
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(5)
    ll.insert_at_end(8)
    ll.insert_at_beginning(6)
    ll.print()
    print("Length of Linked List: ", ll.get_length())
    
    print("\n")
    ll.get_length()
    ll.insert_values(["apple", "tomato", "pickle", "mango", "grapes", "pineapple"])
    ll.print()
    print("Length of Linked List 2: ", ll.get_length())
    ll.remove_at(2)
    ll.print()        
    print("Length of Linked List 2 after removal: ", ll.get_length())
    ll.insert_at(0, "figs")
    ll.print()
    
    print("\n")
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print() 
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()