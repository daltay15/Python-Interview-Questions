# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# Follow up: Could you minimize the total number of operations done?

# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0: # exits loop as soon as all zeros are moved to the end
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
    
    def moveZeroesNoOrder(self, nums):
        last_non_zero = -1 # Set to last element in array
        for i in range(len(nums)):
            if nums[i] != 0:
                last_non_zero += 1
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
        return nums

    def moveZeroesSorted(self, nums):
        last_non_zero = -1 # Set to last element in array
        for i in range(len(nums)):
            if nums[i] != 0:
                last_non_zero += 1
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i] # swap
        non_zero_elements = nums[:last_non_zero+1]  # slice array from 0 to last_non_zero+1
        non_zero_elements_sorted = sorted(non_zero_elements) # sort non-zero elements
        for i in range(len(non_zero_elements_sorted)):
            nums[i] = non_zero_elements_sorted[i]
        return nums
    

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print("Normal",Solution().moveZeroes(nums))
    print("No Order",Solution().moveZeroesNoOrder(nums))
    print("Sorted",Solution().moveZeroesSorted(nums))