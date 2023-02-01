# Reverse a singly linked list.
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):   # Constructor
        self.val = val  # Value
        self.next = next    # Next node

    def __repr__(self): # For printing
        return f"ListNode({self.val},  {self.next})"    # Inorder traversal

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head  # Set the previous node to None and the current node to the head

        while curr: # While the current node is not None
            nxt = curr.next # Store the next node in a temp variable
            curr.next = prev    # Set the next node to the previous node
            prev = curr # Set the previous node to the current node
            curr = nxt  # Set the current node to the next node
        return prev # Return the previous node

if __name__ == "__main__":
    print(Solution().reverseList(head))