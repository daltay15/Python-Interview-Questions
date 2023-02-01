# 167. Two Sum II - Input array is sorted
# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0    # Left pointer
        right = len(numbers) - 1    # Right pointer

        while left < right: # While the left pointer is less than the right pointer
            sum = numbers[left] + numbers[right]    # Get the sum of the left and right pointers

            if sum > target:    # If the sum is greater than the target
                right -= 1  # Move the right pointer left 1
            
            elif sum < target:  # If the sum is less than the target
                left += 1   # Move the left pointer right 1

            else:   # Found the target
                return[left + 1, right  + 1]    # Return the indices of the left and right pointers
                

if __name__ == "__main__":
    List = list
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
