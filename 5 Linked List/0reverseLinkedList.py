# Reverse a singly linked list.
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

if __name__ == "__main__":
    print(Solution().reverseList(head))