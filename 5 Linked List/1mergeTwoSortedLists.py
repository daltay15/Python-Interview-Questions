# Problem: Merge Two Sorted Lists
#
# Approach: Use two pointers to traverse the two lists and compare the values at each pointer. Add the smaller value to the new list and increment the pointer for the list that had the smaller value. If one list is empty, add the remaining values from the other list to the new list.
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + " -> " + str(self.next)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return temp.next
    

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(list1, list2))