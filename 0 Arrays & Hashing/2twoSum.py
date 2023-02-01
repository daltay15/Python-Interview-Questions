# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Empty dictionary

        for i, n in enumerate(nums):    # Iterate through the list
            diff = target - n   # Get the difference between the target and the current number
            if diff in prevMap: # If the difference is in the dictionary
                return [prevMap[diff], i]   # Return the index of the difference and the current index
            prevMap[n] = i  # Add the current number to the dictionary

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))