# Problem: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Create a hashset

        for n in nums:  # Iterate through the list
            if n in hashset:    # If the number is in the hashset
                return True # Return true
            hashset.add(n)  # Add the number to the hashset
        return False    # If the number is not in the hashset

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))