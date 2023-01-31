# 704. Binary Search
# Difficulty: Easy
#
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
# If target exists, then return its index, otherwise return -1.


List = list
nums = [-1,0,3,5,9,12]
target = 9

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2        # Midpoint of the list
            if nums[m] > target:    # if midpoint > target move
                r = m - 1           # Move right pointer left 1
            elif nums[m] < target:  # If midpoint < target
                l = m + 1           # Move left pointer right 1
            else:                   # Found number  
                return m            # Return the position
        return -1

if __name__ == "__main__":
    print(Solution().search(nums, target))