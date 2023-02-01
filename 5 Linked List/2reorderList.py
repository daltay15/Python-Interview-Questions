
# Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes. Only nodes itself may be changed.

# Approach: Find the middle of the list. Reverse the second half of the list. Merge the two halfs.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):   # Constructor
        self.val = val  # Value
        self.next = next    # Next node


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle   
        slow, fast = head, head.next    # Set the slow and fast pointers to the head
        while fast and fast.next:   # While the fast pointer is not None and the next node is not None
            slow = slow.next    # Increment the slow pointer
            fast = fast.next.next   # Increment the fast pointer by 2

        # Reverse the list
        second = slow.next  # Set the second pointer to the next node of the slow pointer
        prev = slow.next = None # Set the next node of the slow pointer to None and set the previous node to None
        while second: # Reverse 2nd portion of list
            temp = second.next  # Store the next node in a temp variable
            second.next = prev  # Set the next node to the previous node
            prev = second   # Set the previous node to the current node
            second = temp   # Set the current node to the next node
        
        # Merge two halfs
        first, second = head, prev  # Set the first and second pointers to the head and the previous node
        while second:   # While the second pointer is not None
            temp1, temp2 = first.next, second.next  # Store the next nodes in temp variables
            first.next = second # Set the next node of the first pointer to the second pointer
            second.next = temp1 # Set the next node of the second pointer to the temp1 variable
            first, second = temp1, temp2   # Set the first and second pointers to the temp variables
