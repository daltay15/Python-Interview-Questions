# Problem: Merge Two Sorted Lists
#
# Approach: Use two pointers to traverse the two lists and compare the values at each pointer. Add the smaller value to the new list and increment the pointer for the list that had the smaller value. If one list is empty, add the remaining values from the other list to the new list.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()   # Create a new list
        tail = temp # Create a tail pointer

        while list1 and list2:  # While both lists are not empty
            if list1.val < list2.val:   # If the value at list1 is smaller than the value at list2
                tail.next = list1   # Add the value at list1 to the new list
                list1 = list1.next  # Increment the pointer for list1
            else:   # If the value at list2 is smaller than the value at list1
                tail.next = list2   # Add the value at list2 to the new list
                list2 = list2.next  # Increment the pointer for list2
            tail = tail.next    # Increment the tail pointer
        
        if list1:   # If list1 is not empty
            tail.next = list1   # Add the remaining values from list1 to the new list
        elif list2: # If list2 is not empty
            tail.next = list2   # Add the remaining values from list2 to the new list

        return temp.next    # Return the new list
    

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(list1, list2))