# Problem: Remove Nth Node From End of List

# Approach: Use two pointers to traverse the list. The first pointer will be n nodes ahead of the second pointer. When the first pointer reaches the end of the list, the second pointer will be at the node before the node to be deleted.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return str(self.val) + " -> " + str(self.next)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Assign right pointer to nth position
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # While right != null iterate through the list
        while right:
            left = left.next
            right = right.next
        
        # Delete the nth node
        left.next = left.next.next  # Skipping over 1 node will delete it, hence .next.next
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print(Solution().removeNthFromEnd(head, n))