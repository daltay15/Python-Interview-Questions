
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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the list
        second = slow.next
        prev = slow.next = None
        while second: # Reverse 2nd portion of list
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two halfs
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
