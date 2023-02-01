# Problem: Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

# time complexity: O(n)
# space complexity: O(1)

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])

        rightMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
            
        return arr

if __name__ == "__main__":
    arr = [17,18,5,4,6,1]
    print(Solution().replaceElements(arr))