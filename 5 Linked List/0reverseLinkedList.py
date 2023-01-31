# Reverse a singly linked list.
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.

# Neetcode Solution
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# VSCode Runnable
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def reverseList(head: ListNode) -> ListNode:
#     prev = None
#     current = head
    
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
        
#     return prev

# # Input: head=[1,2,3,4,5]
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

# # Reverse the linked list
# reversed_head = reverseList(head)

# # Print the reversed linked list
# node = reversed_head
# while node:
#     print(node.val)
#     node = node.next
