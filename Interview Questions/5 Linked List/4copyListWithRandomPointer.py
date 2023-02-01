# 138. Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): # Constructor
        self.val = int(x)   # Value
        self.next = next    # Next node
        self.random = random    # Random node
        
    def __repr__(self):     # For printing
        return str(self.val) + " -> " + str(self.next)  # Inorder traversal
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None }  # Dictionary to store the mapping of old nodes to new nodes

        cur = head  # Current node
        while cur:  # While current node is not null
            copy = Node(cur.val)    # Create a new node with the same value
            oldToCopy[cur] = copy   # Add the mapping to the dictionary
            cur = cur.next  # Increment the current node
        
        cur = head  # Reset the current node
        while cur:  # While current node is not null
            copy = oldToCopy[cur]   # Get the copy of the current node
            copy.next = oldToCopy[cur.next] # Set the next pointer of the copy to the copy of the next node
            copy.random = oldToCopy[cur.random] # Set the random pointer of the copy to the copy of the random node
            cur = cur.next  # Increment the current node
        
        return oldToCopy[head] # Return the head of the copied linked list

        


if __name__ == "__main__":
    head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
    print(Solution().copyRandomList(head))
