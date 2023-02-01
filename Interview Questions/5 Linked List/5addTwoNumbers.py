# Problem: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Approach: Use two pointers to traverse the two lists and compare the values at each pointer. 
# Add the smaller value to the new list and increment the pointer for the list that had the smaller value. 
# If one list is empty, add the remaining values from the other list to the new list.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional

# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next=None):   # Constructor
        self.val = val  # Value
        self.next = next    # Next node
        
    def __repr__(self): # For printing
        return str(self.val) + " -> " + str(self.next)  # Inorder traversal
    
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a new list
        cur = dummy # Create a tail pointer

        carry = 0   # Carry value

        while l1 or l2 or carry:    # While list 1 or list 2 or the carry is not null, will include edge case
            v1 = l1.val if l1 else 0    # If l1 is not null, get the value, else 0
            v2 = l2.val if l2 else 0    # If l2 is not null, get the value, else 0

            # New num
            val = v1 + v2 + carry   # Add the values and the carry
            # 15
            carry = val // 10   # get the 10's place of the value
            val = val % 10    # get the 1's place of the value
            cur.next = ListNode(val)    # Add the value to the new list

            # Update pointers
            cur = cur.next  # Increment the tail pointer
            l1 = l1.next if l1 else None    # Increment the pointer for l1 if l1 is not null, else null
            l2 = l2.next if l2 else None    # Increment the pointer for l2 if l2 is not null, else null
   
        return dummy.next   # Return the new list
    

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(Solution().addTwoNumbers(l1, l2))