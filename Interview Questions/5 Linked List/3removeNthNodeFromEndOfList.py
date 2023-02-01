# Problem: Remove Nth Node From End of List

# Approach: Use two pointers to traverse the list. The first pointer will be n nodes ahead of the second pointer. When the first pointer reaches the end of the list, the second pointer will be at the node before the node to be deleted.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):   # Constructor
        self.val = val  # Value
        self.next = next    # Next node
        
    def __repr__(self): # For printing
        return str(self.val) + " -> " + str(self.next)  # Inorder traversal


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # Dummy node to handle edge cases
        left = dummy    # Left pointer
        right = head    # Right pointer

        # Assign right pointer to nth position
        while n > 0 and right:  # While n > 0 and right != null
            right = right.next  # Increment right pointer
            n -= 1  # Decrement n
        
        # While right != null iterate through the list
        while right:    # While right != null
            left = left.next    # Increment left pointer
            right = right.next  # Increment right pointer
        
        # Delete the nth node
        left.next = left.next.next  # Skipping over 1 node will delete it, hence .next.next
        return dummy.next   # Return the head of the list


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print(Solution().removeNthFromEnd(head, n))